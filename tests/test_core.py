# coding: utf-8
"""
    tests.core
    ~~~~~~~~~~

    Tests the core stuff.

    :copyright: (c) 2015 by Igor Kalnitsky
    :license: MIT, see LICENSE for details
"""

import mock
import unittest

from git_pr.core import PullRequest


@mock.patch('git_pr.core.subprocess.check_call')
class TestPullRequest(unittest.TestCase):

    def setUp(self):
        self.pr = PullRequest('test-repo')

    def test_get(self, sp_call):
        self.pr.get(42)

        self.assertEqual([
            mock.call(['git', 'fetch', 'test-repo', 'pull/42/head']),
            mock.call(['git', 'checkout', 'FETCH_HEAD']),
        ], sp_call.call_args_list)

    def test_get_create_branch(self, sp_call):
        self.pr.get(42, 'pr/42')

        self.assertEqual([
            mock.call(['git', 'fetch', 'test-repo', 'pull/42/head:pr/42']),
            mock.call(['git', 'checkout', 'pr/42']),
        ], sp_call.call_args_list)
