Install the **py-arithmetic** package
=====================================

|cmake| |Documentation Status|

Installation
------------

Install *py-arithmetic* using the bash commands:

.. code-block:: shell-session

    $ git clone https://github.com/chdemko/py-arithmetic.git
    $ cd py-arithmetic
    $ git submodule update --init --recursive
    $ hatch shell

Building
--------

Build *py-arithmetic* using the bash commands:

.. code-block:: shell-session

    $ hatch build
    $ ls dist

Documentation
-------------

Build the documentation using the bash commands:

.. code-block:: shell-session

    $ hatch run docs:build

Testing
-------

Test *py-arithmetic* using the bash commands:

.. code-block:: shell-session

    $ hatch test
    $ hatch fmt --check


.. |cmake| image:: https://github.com/chdemko/py-arithmetic/actions/workflows/python-package.yml/badge.svg
   :target: https://github.com/chdemko/py-arithmetic/actions
.. |Documentation Status| image:: https://img.shields.io/readthedocs/py-arithmetic.svg
   :target: http://py-arithmetic.readthedocs.io/en/latest/?badge=latest
