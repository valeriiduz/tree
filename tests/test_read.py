"""

"""

import io
import os
import shutil
from unittest import TestCase

from tree.Tree import TreeStorage
from PIL import Image


class ReadTest(TestCase):

    def setUp(self):
        self.tree = TreeStorage(os.path.dirname(os.path.abspath(__file__)) + "/storage/")
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        self.tree.insert(file.read())

    def tearDown(self):
        shutil.rmtree(self.tree.path_to_tree)

    def test_read_simple_picture(self):
        self.assertEqual(len(self.tree.show(self.tree.file_hash_name)), 208)
