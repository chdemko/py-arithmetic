Install the **py-arithmetic** package
=====================================

Installation
------------

Install *py-galactic-arithmetic* using the bash command

.. code-block:: shell-session

    $ poetry install --with docs


Documentation
-------------

Build the documentation using the bash commands:

.. code-block:: shell-session

    $ poetry run sphinx-build docs/ build/sphinx/html/

Testing
-------

Test *py-galactic-arithmetic* using the bash command:

.. code-block:: shell-session

    $ poetry run tox
    $ poetry run tox -e style
    $ poetry run tox -e linter

