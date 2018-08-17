import os
from .Helpers import hash_to_path, hash_name_generator


class TreeStorage:
    """
    Main object for the manipulate of the tree storage
    """

    def __init__(self, path_to_tree=None):
        """
        When initialize TreeStorage client
        must be write path to storage
        """

        self.file_hash_name = None

        if not path_to_tree:
            raise ValueError('Path to tree must be initialize')
        self.path_to_tree = path_to_tree
    
    def insert(self, file_byte, mode='wb'):
        """
        Insert file to the data tree storage
        """
        self.file_hash_name = hash_name_generator()
        hash_dir = hash_to_path(hash_name=self.file_hash_name)
        path_hash = self.path_to_tree + hash_dir
        os.makedirs(path_hash)
        with open(os.path.join(path_hash, self.file_hash_name),
                  mode=mode) as file_hash:
            return file_hash.write(file_byte)

    def update(self, file_hash_name, file_byte, mode='wb'):
        """
        Rewrite file in the data tree storage
        """
        hash_dir = hash_to_path(hash_name=file_hash_name)
        with open(os.path.join(self.path_to_tree, hash_dir,
                               file_hash_name), mode=mode) as file_hash:
            return file_hash.write(file_byte)

    def remove(self, file_hash_name):
        """
        Remove file from the tree storage
        """
        path_hash = hash_to_path(hash_name=file_hash_name)
        path = os.path.join(self.path_to_tree, path_hash, file_hash_name)
        return os.remove(path)

    def show(self, file_hash_name):
        """
        Show file byte from the tree storage
        """
        path_hash = hash_to_path(hash_name=file_hash_name)
        return os.path.join(self.path_to_tree, path_hash, file_hash_name)
