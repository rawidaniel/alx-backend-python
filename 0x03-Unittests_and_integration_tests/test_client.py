#!/usr/bin/env python3
"""
Module test_client
"""

import unittest
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    A class that represent test for GithubOrg client
    """
    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org, mock_get_json):
        """Test org function

        Parameters
        ----------
        org: str
          organization name
        mock_get_json: mock object
            mock object of get_json
        """
        githubClient = GithubOrgClient(org)
        test_response = githubClient.org
        self.assertEqual(test_response, mock_get_json.return_value)
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """Test the result of _public_repos_url as expected
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            test_payload = {"repos_url":
                            "https://api.github.com/orgs/google/repos"}
            githubOrgClient = GithubOrgClient("google")
            mock_org.return_value = test_payload
            test_response = githubOrgClient._public_repos_url
            self.assertEqual(test_response,
                             mock_org.return_value.get("repos_url"))
            mock_org.assert_called_once()

    @patch("client.get_json", return_value=[{'name': 'Holberton'},
                                            {'name': '89'},
                                            {'name': 'alx'}])
    def test_public_repos(self, mock_get_json):
        """Test the result of public_repos as expected

        mock_get_json: mock object
            mock object of get_json
        """
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos:
            test_payload = "https://api.github.com/orgs/google/repos"
            mock_public_repos.return_value = test_payload
            githubOrgClient = GithubOrgClient("google")
            test_result = githubOrgClient.public_repos()
            self.assertEqual(test_result,
                             [obj["name"]
                              for obj in mock_get_json.return_value])
            mock_get_json.assert_called_once()
            mock_public_repos.assert_called_once()

    @parameterized.expand([({"license": {"key": "my_license"}},
                            "my_license", True),
                          ({"license": {"key": "other_license"}},
                          "my_license", False)])
    def test_has_license(self, repo, license_key, result):
        """Test the result of has_license as expected
        Parameters
        ----------
        repo: Mapping
          nested mapping
        license_key: str
          licence key of host website
        result: bool
          the result of has_license function
        """
        test_response = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(test_response, result)


def requests_get(*args, **kwargs):
    """
    Function that mocks requests.get function
    Returns the correct json data based on the given input url
    """
    class MockResponse:
        """
        Mock response
        """
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

    if args[0] == "https://api.github.com/orgs/google":
        return MockResponse(TEST_PAYLOAD[0][0])
    if args[0] == TEST_PAYLOAD[0][0]["repos_url"]:
        return MockResponse(TEST_PAYLOAD[0][1])


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1], TEST_PAYLOAD[0][2],
      TEST_PAYLOAD[0][3])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for the GithubOrgClient.public_repos method
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up function for TestIntegrationGithubOrgClient class
        Sets up a patcher to be used in the class methods
        """
        cls.get_patcher = patch('requests.get', side_effect=requests_get)
        cls.get_patcher.start()
        cls.client = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls):
        """
        Tear down resources set up for class tests.
        Stops the patcher that had been started
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method without license
        """
        self.assertEqual(self.client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos method with license
        """
        self.assertEqual(
            self.client.public_repos(license="apache-2.0"),
            self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
