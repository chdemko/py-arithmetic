Install the **py-arithmetic** package
=====================================

|cmake| |Documentation Status|

Installation
------------

Install *py-arithmetic* using the bash command

.. code-block:: shell-session

    $ poetry install --with docs


Documentation
-------------

Build the documentation using the bash commands:

.. code-block:: shell-session

    $ poetry run sphinx-build docs/ build/sphinx/html/

Testing
-------

Test *py-arithmetic* using the bash command:

.. code-block:: shell-session

    $ poetry run tox
    $ poetry run tox -e style
    $ poetry run tox -e linter


.. |cmake| image:: https://github.com/chdemko/py-arithmetic/actions/workflows/python-package.yml/badge.svg
   :target: https://github.com/chdemko/py-arithmetic/actions
.. |Documentation Status| image:: https://img.shields.io/readthedocs/py-arithmetic.svg
   :target: http://py-arithmetic.readthedocs.io/en/latest/?badge=latest
