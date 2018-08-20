# Tree

[![Build status](https://ci.appveyor.com/api/projects/status/q3qla5acuod7opsc/branch/master?svg=true)](https://ci.appveyor.com/project/valeriiduz/tree/branch/master)
[![Build Status](https://travis-ci.org/valeriiduz/Tree.svg?branch=master)](https://travis-ci.org/valeriiduz/Tree)
[![Build s](https://readthedocs.org/projects/tree/badge/?version=latest)]()

## Overview

Tree - it the library for who wants to save a large number of files.
For preservation it is enough to you to transfer a binary code of the file and the Tree will keep him.

![Tree image](https://raw.githubusercontent.com/valeriiduz/Tree/master/docs/_static/tree.jpg)

## Example

Superficial uses in the tree hash storage
```python
from tree import TreeStorage

tree = TreeStorage("/path/to/storage")

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
```

## Installing

[![Python Version](https://img.shields.io/pypi/pyversions/tree-storage.svg)]()
[![Build s](https://img.shields.io/pypi/v/tree-storage.svg)]()

PyPy and PyPy3 are also supported (and tested against).

Download and install the latest released version from PyPI:
```bash
pip install tree-storage
```

Download and install the development version from GitHub:
```bash
pip install git+https://github.com/valeriiduz/Tree
```

Installing from source (installs the version in the current working directory):
```bash
python setup.py install
```

(In all cases, add --user to the install command to install in the current user's home directory.)
Install and Update Tree library using pip:

## Documentation

Read full documentation on [https://tree.readthedocs.io/](https://tree.readthedocs.io/).

## License

This repository is distributed under The MIT license
