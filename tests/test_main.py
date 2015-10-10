# coding: utf-8
"""
    tests.main
    ~~~~~~~~~~

    Tests CLI.

    :copyright: (c) 2015 by Igor Kalnitsky
    :license: MIT, see LICENSE for details
"""

import mock
import unittest

from git_pr.__main__ import main


@mock.patch('git_pr.__main__.PullRequest', autospec=True)
class TestCLI(unittest.TestCase):

    def test_one_argument(self, PullRequest):
        main(['42'])

        PullRequest.assert_called_once_with('origin')
        PullRequest('origin').get.assert_called_once_with(42, None)

    def test_two_arguments(self, PullRequest):
        main(['github', '42'])

        PullRequest.assert_called_once_with('github')
        PullRequest('github').get.assert_called_once_with(42, None)

    def test_branch_argument(self, PullRequest):
        main(['42', '-b', 'pr/42'])

        PullRequest.assert_called_once_with('origin')
        PullRequest('origin').get.assert_called_once_with(42, 'pr/42')
