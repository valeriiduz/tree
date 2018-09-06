"""
Tree Hash Storage

Tree hash-storage of a large number of files

Tree - it the library for who wants to save
a large number of files. For preservation
it is enough to you to transfer a binary code
of the file and the Tree will keep him.

:copyright: Copyright 2011-2014 Valerii Duz.
:license: MIT, see LICENSE for details.
"""

import sys

if sys.version_info.major < 3:
    raise RuntimeError(
        'Tree does not support Python 2.x. '
        'Please use Python 3.')

__title__ = 'tree-storage'
__version__ = '0.0.12'
__author__ = 'Valerii Duz'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018 ValeriiDuz'
