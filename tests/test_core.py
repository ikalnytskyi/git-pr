# coding: utf-8
"""
    tests.core
    ~~~~~~~~~~

    Tests the core stuff.

    :copyright: (c) 2015 by Ihor Kalnytskyi
    :license: MIT, see LICENSE for details
"""

import mock
import unittest

from git_pr.core import PullRequest


@mock.patch('git_pr.core.subprocess.check_call')
class TestPullRequest(unittest.TestCase):

    def setUp(self):
        self.pr = PullRequest('repo')

    def test_get(self, sp_call):
        self.pr.get(42)

        self.assertEqual([
            mock.call(['git', 'fetch', 'repo', 'refs/pull/42/head']),
            mock.call(['git', 'checkout', 'FETCH_HEAD']),
        ], sp_call.call_args_list)

    def test_get_create_branch(self, sp_call):
        self.pr.get(42, 'pr/42')

        self.assertEqual([
            mock.call(['git', 'fetch', 'repo', 'refs/pull/42/head:pr/42']),
            mock.call(['git', 'checkout', 'pr/42']),
        ], sp_call.call_args_list)

    def test_get_merge_commit(self, sp_call):
        self.pr.get(42, merge=True)

        self.assertEqual([
            mock.call(['git', 'fetch', 'repo', 'refs/pull/42/merge']),
            mock.call(['git', 'checkout', 'FETCH_HEAD']),
        ], sp_call.call_args_list)

    def test_get_create_branch_and_merge_commit(self, sp_call):
        self.pr.get(42, 'pr/42', merge=True)

        self.assertEqual([
            mock.call(['git', 'fetch', 'repo', 'refs/pull/42/merge:pr/42']),
            mock.call(['git', 'checkout', 'pr/42']),
        ], sp_call.call_args_list)

    def test_get_no_checkout(self, sp_call):
        self.pr.get(42, no_checkout=True)

        self.assertEqual([
            mock.call(['git', 'fetch', 'repo', 'refs/pull/42/head']),
        ], sp_call.call_args_list)

    def test_get_create_branch_and_no_checkout(self, sp_call):
        self.pr.get(42, 'pr/42', no_checkout=True)

        self.assertEqual([
            mock.call(['git', 'fetch', 'repo', 'refs/pull/42/head:pr/42']),
        ], sp_call.call_args_list)
