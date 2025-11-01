Install the *py-arithmetic* package
===================================

|cmake| |Documentation Status|

Installation
------------

Install *py-arithmetic* using the **bash** commands:

.. code-block:: bash

    $ git clone https://github.com/chdemko/py-arithmetic.git
    $ cd py-arithmetic
    $ git submodule update --init --recursive
    $ hatch shell

Building
--------

Build *py-arithmetic* using the **bash** commands:

.. code-block:: bash

    $ hatch build
    $ ls dist
    $ unzip -v dist/py_arithmetic-*.whl

Note that there is a compiled version of the source files written in the **C** language
within the **Python** `whl` package.

Documentation
-------------

Build the documentation using the **bash** commands:

.. code-block:: bash

    $ hatch run docs:build

Then, open the generated HTML documentation in your web browser:

.. code-block:: bash

    $ xdg-open build/sphinx/html/index.html

Testing
-------

Test *py-arithmetic* using the bash commands:

.. code-block:: bash

    $ hatch test
    $ hatch fmt --check

.. |cmake| image:: https://github.com/chdemko/py-arithmetic/actions/workflows/python-package.yml/badge.svg
   :target: https://github.com/chdemko/py-arithmetic/actions
.. |Documentation Status| image:: https://img.shields.io/readthedocs/py-arithmetic.svg
   :target: http://py-arithmetic.readthedocs.io/en/latest/?badge=latest
