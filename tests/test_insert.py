"""

"""
import io
import os
import shutil
from unittest import TestCase
from PIL import Image

from tree import TreeStorage


class InsertTest(TestCase):

    def setUp(self):
        self.tree = TreeStorage(os.path.dirname(os.path.abspath(__file__)) + "/storage/")

    def tearDown(self):
        shutil.rmtree(self.tree.path_to_tree)

    def test_insert_simple_picture(self):
        """
        Test upload simple picture
        """
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        status_insert = self.tree.breed(file.read())
        self.assertEqual(status_insert, 315)
