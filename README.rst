Tree
====

.. image:: https://travis-ci.org/valeriiduz/Tree.svg?branch=master
   :alt: Build status
   :target: https://travis-ci.org/valeriiduz/Tree

.. image:: https://readthedocs.org/projects/tree/badge/?version=latest
   :alt: Documentation
   :target: https://readthedocs.org/projects/tree/badge/?version=latest

Overview
~~~~~~~~

Tree the library for saving a large number of files.
For preservation it is enough to you to transfer a binary code of the file and the Tree will keep him.

.. image:: https://raw.githubusercontent.com/valeriiduz/Tree/master/docs/_static/tree.jpg
   :height: 100
   :width: 200
   :scale: 50
   :alt: Tree image

Example
~~~~~~~

Superficial uses in the tree hash storage
::
    from tree.tree import TreeStorage
    from tree.config import TreeConfig

    # Initialize config for the TreeStorage
    config = TreeConfig({
        "PATH_TO_TREE": "/path/to/storage"
    })

    tree = TreeStorage(config)

    # If you want add file to the Tree Storage
    with open("/path/to/file", "rb") as file:
        tree.breed(file_byte=file.read(), mode='wb')
    # after add file, method return status of writing. 
    # If add file status is success, tree save last 
    # hash of the file in the attribute file_hash_name

    # For remove file from the Tree Storage
    # you can call cut method and past 
    # to him hash name of file which you have delete
    tree.cut(file_hash_name=tree.file_hash_name, greedy=True)

Installing
~~~~~~~~~~

.. image:: https://img.shields.io/pypi/pyversions/tree-storage.svg
   :alt: Python Version
   :target: https://img.shields.io/pypi/pyversions/tree-storage.svg

.. image:: https://img.shields.io/pypi/v/tree-storage.svg
   :alt: Project Version
   :target: https://img.shields.io/pypi/v/tree-storage.svg

PyPy and PyPy3 are also supported (and tested against).

Download and install the latest released version from PyPI:
::
    pip install tree-storage

Download and install the development version from GitHub:
::
    pip install git+https://github.com/valeriiduz/Tree

Installing from source (installs the version in the current working directory):
::
    python setup.py install


(In all cases, add --user to the install command to install in the current user's home directory.)
Install and Update Tree library using pip:

Documentation
~~~~~~~~~~~~~

Read full documentation on `https://tree.readthedocs.io/ <https://tree.readthedocs.io/>`_.

License
~~~~~~~

This repository is distributed under The MIT license
