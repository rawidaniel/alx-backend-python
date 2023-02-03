#!/usr/bin/env python3
"""
Module test_client
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


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


if __name__ == "__main__":
    unittest.main()
