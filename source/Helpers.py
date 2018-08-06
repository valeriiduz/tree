'''
Split helpers function for the Tree library
'''

import os
import sys
import random
import hashlib


def hash_to_path(hashName=None):
    '''
    Convert hashName to directory path
    '''
    dirPath = ''.join([f'{symbol}/' if idx % 2 else f'{symbol}' for idx, symbol in enumerate(hashName)])[:-1]
    return dirPath



def hash_name():
    hash = hashlib.sha256(bytes(int(random.random()*100000))).hexdigest()
    return hash
