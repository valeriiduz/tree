"""
Split helpers function for the Tree library
"""

import random
import hashlib


def slice_hash(func):
    """
    Slice hash path to the dir path and file name
    """
    def _(*args, **kwargs):
        hash_path = func(*args, **kwargs)
        return hash_path[:-3], hash_path[-3:-1]
    return _


@slice_hash
def hash_to_path(hash_name=''):
    """
    Convert hash name to directory path
    """
    return ''.join(['{}/'.format(symbol) if idx % 2 else '{}'.format(symbol) for idx, symbol in enumerate(hash_name)])


def hashing_file(file_byte=b'', algorithm='sha256'):
    """
    Hashing file from file bytes
    """
    return getattr(hashlib, algorithm)(file_byte).hexdigest()


def hash_name_generator(algorithm="sha256"):
    """
    Generating hash name from random bytes
    """
    random_bytes = bytes(int(random.random()*100000))
    return getattr(hashlib, algorithm)(random_bytes).hexdigest()
