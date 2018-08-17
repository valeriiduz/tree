"""
Tree

Tree hash storage

:copyright: Copyright 2011-2014 Valerii Duz.
:license: MIT, see LICENSE for details.
"""

import sys

if sys.version_info.major < 3:
    raise RuntimeError(
        'Tree does not support Python 2.x. '
        'Please use Python 3.')

VERSION = '0.0.1'
VERSION_STRING = 'Tree %s (https://tree.readthedocs.io/)' % VERSION

__version__ = VERSION
__all__ = ['VERSION']


from .Tree import (TreeStorage)
