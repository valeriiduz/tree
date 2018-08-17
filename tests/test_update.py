"""

"""
import io
import os
import shutil
from unittest import TestCase

from PIL import Image

from tree.Tree import TreeStorage


class UpdateTest(TestCase):

    def setUp(self):
        self.tree = TreeStorage(os.path.dirname(os.path.abspath(__file__)) + "/storage/")

    def tearDown(self):
        shutil.rmtree(self.tree.path_to_tree)

    def test_update_picture_to_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        status_insert_first_file = self.tree.insert(file.read())
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(0, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        status_update_first_file = self.tree.update(self.tree.file_hash_name, file.read())
        self.assertNotEqual(status_insert_first_file, status_update_first_file)
