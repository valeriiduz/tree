"""

"""
import io
import os
import shutil
from unittest import TestCase

from PIL import Image

from tree.tree import TreeStorage
from tree.utils import hash_name_generator
from tree.config import TreeConfig


class TreeCutTest(TestCase):

    def setUp(self):
        self.config = TreeConfig({
            "PATH_TO_TREE": os.path.dirname(os.path.abspath(__file__)) + "/storage/"
        })
        self.tree = TreeStorage(config=self.config)

    def tearDown(self):
        shutil.rmtree(self.config.PATH_TO_TREE)

    def test_remove_simple_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        self.tree.breed(file.read())
        status_remove = self.tree.cut(self.tree.file_hash_name)
        self.assertEqual(status_remove, None)

    def test_cut_non_exist_file(self):
        self.assertNotEqual(self.tree.cut(hash_name_generator()), None)
