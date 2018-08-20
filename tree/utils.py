"""
Split helpers function for the Tree library
"""

import random
import hashlib


def hash_to_path(hash_name=''):
    """
    Convert hashName to directory path
    """
    path = ''.join([f'{symbol}/' if idx % 2 else f'{symbol}' for idx, symbol in enumerate(hash_name)])
    return path[:-3], path[-3:-1]


def hashing_file(file_byte=b'', algorithm='sha256'):
    """
    Hash file from file byte
    """
    file_hash = getattr(hashlib, algorithm)(file_byte).hexdigest()
    return file_hash


def hash_name_generator(algorithm="sha256"):
    """
    Generating hash name
    """
    random_bytes = bytes(int(random.random()*100000))
    print(type(algorithm))
    hash_name = getattr(hashlib, algorithm)(random_bytes).hexdigest()
    return hash_name
