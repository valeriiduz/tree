# Tree

[![Build status](https://ci.appveyor.com/api/projects/status/q3qla5acuod7opsc/branch/master?svg=true)](https://ci.appveyor.com/project/valeriiduz/tree/branch/master)
[![Build Status](https://travis-ci.org/valeriiduz/Tree.svg?branch=master)](https://travis-ci.org/valeriiduz/Tree)
[![Build s](https://readthedocs.org/projects/tree/badge/?version=latest)]()

## Overview

Tree - it the library for who wants to save a large number of files.
For preservation it is enough to you to transfer a binary code of the file and the Tree will keep him.

![Tree image](https://raw.githubusercontent.com/valeriiduz/Tree/master/docs/_static/tree.jpg)

## Example

Superficial uses of CRUD functions in the tree hash storage
```python
from tree.Tree import TreeStorage

tree = TreeStorage("/path/to/storage")

# For add file to the Tree storage
# after add file, insert method return status of
# writing in the tree. If add file status is success,
# tree save last file hash name in the attribute file_hash_name
with open("/path/to/file", "rb") as file:
    tree.insert(file.read())

# View full path to file in the storage 
# you can call show method and paste hash name 
# of file which you search
tree.show(tree.file_hash_name)

# if you have to update the existing file
# simple call update method and write in 
# arguments hash name of the file which 
# you have to update and blob of new file
with open("/path/to/second_file", "rb") as file:
    tree.update(tree.file_hash_name, file.read())
    
# Remove file from the Tree Storage
# you can call remove method and past 
# to him hash name of file which you have delete
tree.remove(tree.file_hash_name)

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
