# coding: utf-8
"""
    git-pr.__main__
    ~~~~~~~~~~~~~~~

    The module provides a command line interface implementation.

    :copyright: (c) 2015 by Ihor Kalnytskyi
    :license: MIT, see LICENSE for details
"""

import sys
import argparse
import subprocess

from git_pr.core import PullRequest


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(prog='git pr')

    parser.add_argument(
        'repository', nargs='?',
        default='origin',
        help='a repository to fetch pull request from')

    parser.add_argument(
        'pull_request',
        type=int,
        help='a pull request to be fetched')

    parser.add_argument(
        '-b', '--branch',
        help='create a branch if passed')

    parser.add_argument(
        '-m', '--merge', action='store_true',
        help='fetch merge commit if passed')

    parser.add_argument(
        '-C', '--no-checkout', action='store_true',
        help='do not auto switch to fetched pull request ')

    arguments = parser.parse_args(args)

    try:
        pr = PullRequest(arguments.repository)
        pr.get(
            arguments.pull_request,
            arguments.branch,
            arguments.merge,
            arguments.no_checkout)

    except subprocess.CalledProcessError:
        # do nothing, just because that mostly means we do have an error
        # from git binary on stderr and it makes no sense to continue or
        # print custom error
        sys.exit(1)


# let's make this module and git_pr package to be executable,
# so anyone would be able to run it without entry_points'
# console script
if __name__ == '__main__':
    main()
