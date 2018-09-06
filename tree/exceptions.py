"""

"""


class TreeConfigNotExist(Exception):
    """
    Error class if storage initialize without config parameter
    """
    def __init__(self):
        self.args = "Storage initialize must be have a config variable"


class TreeFileNonExist(FileNotFoundError):
    """
    Error class if hash non exist in tree storage
    """
    def __init__(self, file_hash_name):
        self.msg = "File with such hash is not found: {}".format(file_hash_name)
