"""
Tree

Tree hash storage

:copyright: Copyright 2011-2014 Valerii Duz.
:license: MIT, see LICENSE for details.
"""

import sys

from .tree import TreeStorage
from .utils import *

if sys.version_info.major < 3:
    raise RuntimeError(
        'Tree does not support Python 2.x. '
        'Please use Python 3.')

__all__ = ['TreeStorage']
