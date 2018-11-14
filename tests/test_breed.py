"""
Testing add file to the storage
"""

import io
import os
import shutil
from unittest import TestCase
from PIL import Image

from tree.tree import TreeStorage
from tree.config import TreeConfig


class TreeBreedTest(TestCase):

    def setUp(self):
        self.config = TreeConfig({
            "PATH_TO_TREE": os.path.dirname(os.path.abspath(__file__)) + "/storage/"
        })
        self.tree = TreeStorage(config=self.config)

    def tearDown(self):
        shutil.rmtree(self.config.PATH_TO_TREE)

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
