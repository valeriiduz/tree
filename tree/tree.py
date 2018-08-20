import os
from .utils import hash_to_path, \
    hashing_file


class TreeStorage:
    """
    Main object for the manipulate of the tree storage
    """

    def __init__(self, path_to_tree=None):
        """
        When initialize TreeStorage client
        must be write path to storage
        """
        if not path_to_tree:
            raise ValueError('Path to tree must be initialize')

        self.path_to_tree = path_to_tree
        self.file_hash_name = None

    def breed(self, file_byte, mode='wb'):
        """
        Insert file to the data tree storage
        """
        self.file_hash_name = hashing_file(file_byte)
        hash_dir, hash_file = hash_to_path(hash_name=self.file_hash_name)
        os.makedirs(self.path_to_tree + hash_dir)
        with open(os.path.join(self.path_to_tree, hash_dir, hash_file),
                  mode=mode) as file_hash:
            return file_hash.write(file_byte)

    def cut(self, file_hash_name, greedy=False):
        """
        Remove file from the tree storage
        """
        if greedy:
            pass  # TODO: if dir is empty must be remove
        hash_dir, hash_file = hash_to_path(hash_name=file_hash_name)
        path = os.path.join(self.path_to_tree, hash_dir, hash_file)
        return os.remove(path)