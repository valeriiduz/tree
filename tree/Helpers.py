"""
Split helpers function for the Tree library
"""

import random
import hashlib


def hash_to_path(hash_name):
    """
    Convert hashName to directory path
    :param hash_name:
    :return:
    """
    path = ''.join([f'{symbol}/' if idx % 2 else f'{symbol}' for idx, symbol in enumerate(hash_name)])[:-1]
    return path


def hash_name():
    hash = hashlib.sha256(bytes(int(random.random()*100000))).hexdigest()
    return hash
