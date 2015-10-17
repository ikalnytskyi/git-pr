==============
 Installation
==============

This part of the documentation covers the installation of ``git-pr``. The
first step to using any software package is getting it properly installed.

Requirements
============

=============  =======  =======  =======  =======  =======  =======
 OS / Python     2.7      3.2      3.3      3.4      3.5     pypy
=============  =======  =======  =======  =======  =======  =======
   Linux         yes      yes      yes      yes      yes     maybe
-------------  -------  -------  -------  -------  -------  -------
   OS X          yes      yes      yes      yes      yes     maybe
-------------  -------  -------  -------  -------  -------  -------
   Windows      maybe    maybe    maybe    maybe    maybe    maybe
=============  =======  =======  =======  =======  =======  =======

.. note::

   In the table above, **maybe** means that the project should work fine
   with proper installation. However, the configuration isn't a part of
   testing gates on CI, so there's no guarantee it works.


Install via pip
===============

A universal installation method that works on Linux, OS X and even Windows.

.. code:: bash

    $ [sudo] pip install git-pr
