"""

"""
import io
import os
import shutil
from unittest import TestCase

from PIL import Image

from tree import TreeStorage


class RemoveTest(TestCase):

    def setUp(self):
        self.tree = TreeStorage(os.path.dirname(os.path.abspath(__file__)) + "/storage/")

    def tearDown(self):
        shutil.rmtree(self.tree.path_to_tree)

    def test_remove_simple_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        self.tree.breed(file.read())
        status_remove = self.tree.cut(self.tree.file_hash_name)
        self.assertEqual(status_remove, None)
