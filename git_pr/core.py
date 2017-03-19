# coding: utf-8
"""
    git-pr.core
    ~~~~~~~~~~~

    The module contains a core stuff that's used by CLI to manage
    GitHub's pull requests.

    :copyright: (c) 2015 by Ihor Kalnytskyi
    :license: MIT, see LICENSE for details
"""

import subprocess


class PullRequest(object):

    def __init__(self, repository):
        self._repository = repository

    def get(self, pr, branch=None, merge=False, no_checkout=False):
        pointer = 'head' if not merge else 'merge'
        refspec = 'refs/pull/{0}/{1}'.format(pr, pointer)

        if branch is not None:
            refspec = '{0}:{1}'.format(refspec, branch)
        subprocess.check_call(['git', 'fetch', self._repository, refspec])

        if not no_checkout:
            # FETCH_HEAD stores a reference to the latest fetched commit,
            # so let's use it if branch isn't specified
            subprocess.check_call(['git', 'checkout', branch or 'FETCH_HEAD'])
