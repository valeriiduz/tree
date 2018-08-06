"""
Tree library
"""

import os
import shutil

from .Helpers import hash_to_path, hash_name


class TreeStorage:

    def __init__(self, path_to_tree=None):

        self.file_hash_name = None

        if not path_to_tree:
            raise ValueError('Path to tree must be initialize')
        self.path_to_tree = path_to_tree
    
    def insert(self, file_byte):
        """
        Insert file to the data tree
        """
        self.file_hash_name = hash_name()
        hash_dir = hash_to_path(hash_name=self.file_hash_name)
        path_hash = self.path_to_tree + hash_dir
        os.makedirs(path_hash)
        with open(os.path.join(path_hash, self.file_hash_name), 'wb') as file_hash:
            return file_hash.write(file_byte)

    def update(self, hash_name, file_byte):
        """
        Rewrite file in the data tree
        """
        hash_dir = hash_to_path(hash_name=hash_name)
        with open(os.path.join(self.path_to_tree, hash_dir, hash_name), 'wb') as file_hash:
            file_hash.write(file_byte)

    def remove(self, file_hash_name):
        """
        Remove file from the tree storage
        """
        path_hash = hash_to_path(hash_name=file_hash_name)
        path = self.path_to_tree + path_hash
        shutil.rmtree(path)

    def read(self, file_hash, format='byte'):
        """
        Show file byte from the tree storage
        """
        path_hash = hash_to_path(hash_name=file_hash)

        mode = "rb" if format == "byte" else "r"

        with open(os.path.join(self.path_to_tree, path_hash, file_hash), mode) as file_byte:
            return file_byte

