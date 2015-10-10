# coding: utf-8
"""
    git-pr.core
    ~~~~~~~~~~~

    The module contains a core stuff that's used by CLI to manage
    GitHub's pull requests.

    :copyright: (c) 2015 by Igor Kalnitsky
    :license: MIT, see LICENSE for details
"""

import subprocess


class PullRequest(object):

    def __init__(self, repository):
        self._repository = repository

    def get(self, pr, branch=None):
        refspec = 'pull/{0}/head'.format(pr)
        if branch is not None:
            refspec = '{0}:{1}'.format(refspec, branch)
        subprocess.check_call(['git', 'fetch', self._repository, refspec])

        # FETCH_HEAD stores a reference to the latest fetched commit,
        # so let's use it if branch isn't specified
        subprocess.check_call(['git', 'checkout', branch or 'FETCH_HEAD'])
