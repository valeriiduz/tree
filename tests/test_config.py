"""
Testing TreeConfig class with
different dict params
"""

from unittest import TestCase
from tree.config import TreeConfig


class TreeConfigTest(TestCase):

    def test_initialize_with_dict(self):
        config = TreeConfig(params={
            "PATH_TO_TREE": "/path/to/tree"
        })
        self.assertEqual(config.PATH_TO_TREE, "/path/to/tree")

    def test_initialize_with_kwargs(self):
        config = TreeConfig(PATH_TO_TREE="/path/to/tree")
        self.assertEqual(config.PATH_TO_TREE, "/path/to/tree")

    def test_initialize_with_dict_and_kwargs(self):
        config = TreeConfig(params={
            "PATH_TO_TREE": "/path/to/tree"
        }, PATH_TO_TREE="/path/to/tree/second")
        self.assertEqual(config.PATH_TO_TREE, "/path/to/tree/second")
