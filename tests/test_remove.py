"""

"""

import os
import shutil
from unittest import TestCase

from tree.Tree import TreeStorage


class RemoveTest(TestCase):

    def setUp(self):
        self.tree = TreeStorage(os.path.dirname(os.path.abspath(__file__)) + "/storage/")

    def tearDown(self):
        shutil.rmtree(self.tree.path_to_tree)
