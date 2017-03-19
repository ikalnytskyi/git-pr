# coding: utf-8
"""
    tests.main
    ~~~~~~~~~~

    Tests CLI.

    :copyright: (c) 2015 by Ihor Kalnytskyi
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
        PullRequest('origin').get.assert_called_once_with(
            42, None, False, False
        )

    def test_two_arguments(self, PullRequest):
        main(['github', '42'])

        PullRequest.assert_called_once_with('github')
        PullRequest('github').get.assert_called_once_with(
            42, None, False, False
        )

    def test_branch_argument(self, PullRequest):
        main(['42', '-b', 'pr/42'])

        PullRequest.assert_called_once_with('origin')
        PullRequest('origin').get.assert_called_once_with(
            42, 'pr/42', False, False
        )

    def test_merge_commit_argument(self, PullRequest):
        main(['42', '-m'])

        PullRequest.assert_called_once_with('origin')
        PullRequest('origin').get.assert_called_once_with(
            42, None, True, False
        )

    def test_no_checkout_argument(self, PullRequest):
        main(['42', '--no-checkout'])

        PullRequest.assert_called_once_with('origin')
        PullRequest('origin').get.assert_called_once_with(
            42, None, False, True
        )
