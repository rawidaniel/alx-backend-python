#!/usr/bin/env python3
"""
Module test_client
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch


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


if __name__ == "__main__":
    unittest.main()
