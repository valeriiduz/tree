"""
Split helpers function for the Tree library
"""

import random
import hashlib


def hash_to_path(hash_name=''):
    """
    Convert hashName to directory path
    """
    return ''.join([f'{symbol}/' if idx % 2 else f'{symbol}' for idx, symbol in enumerate(hash_name)])[:-1]


def hash_name_generator(algorithm='sha256'):
    """
    Generating hash name
    """
    random_bytes = bytes(int(random.random()*100000))
    hash_name = getattr(hashlib, algorithm)(random_bytes).hexdigest()
    return hash_name
