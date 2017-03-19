=======
 Usage
=======

``git-pr`` provides a simple command line interface with the following
synopsis:

.. code::

    git pr [repository] pull_request [--branch test]


Fetch
=====

Usually you just need to run the following short command in order to fetch
pull request with ID=42:

.. code:: bash

    $ git pr 42

When it's done, you'll be automatically switched to fetched commit(s).

.. note::

   By default, the ``origin`` remote is assumed. So please make sure it
   points to GitHub, otherwise the command will fail.


Fetch From Remote
=================

Sometimes ``origin`` remote is configured to point to some internal or
private repo. In this case you must specify **explicitly** remote that
points to GitHub mirror:

.. code:: bash

    $ git pr github 42

It behaves exactly like the command above, but unlike last one the ``github``
remote will be used instead of ``origin``.


Fetch From URL
==============

If, by some reason, you don't have a remote pointed to GitHub, you can
specify repo URL instead:

.. code:: bash

    $ git pr https://github.com/ikalnitsky/git-pr.git 42


Fetch To New Branch
===================

By default, you're in **detached** state after fetching. So if you switch
to other branch in order to do some work you won't be able to switch back.

That's why ``git-pr`` supports a way to fetch a pull request into a new
branch. In order to do so you have to pass either ``-b`` or ``--branch``
argument with a branch name:

.. code:: bash

    $ git pr 42 -b pr/42

When it's done, the ``pr/42`` local branch is created with content of the
pull request with ID=42.


Fetch Merge Commit
==================

Each pull request produces two refs:

  * one, that points to submitted pull request as its author submitted it;
  * one, that points to a merge commit of a pull request and a branch it's
    submitted to;

By default, ``git-pr`` fetches the first one. If you want to fetch the second
one, you've got to pass either ``-m`` or  ``--merge`` argument:

.. code:: bash

    $ git pr 42 --merge


Fetch Without Checkout
======================

By default, when a pull request is fetched, ``git-pr`` automatically checkouts
to the fetched copy. It's not something you always want, so if you need to
turn it off just pass either ``-C`` or ``--no-checkout`` argument:

.. code:: bash

    $ git pr 42 --no-checkout
