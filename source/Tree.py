"""
Tree library
"""

import os

from .Helpers import hash_to_path, hash_name

class Tree:

    def __init__(self, pathToTree=None):

        if not pathToTree:
            raise ValueError('Path to tree must be inizialize')
        self.pathToTree = pathToTree
    
    def insert(self, fileByte):
        '''
        Insert file to the data tree
        '''
        hashName = hash_name()
        hashDir = hash_to_path(hashName)
        pathHash = self.pathToTree + hashDir
        os.makedirs(pathHash)
        with open(os.path.join(pathHash, hashName), 'wb') as fileHash:
            fileHash.write(fileByte)

    def update(self, fileHash, fileByte):
        '''
        Rewrite file in the data tree
        '''
        with open(os.path.join(dirPath, hashName), 'wb') as fileByte:
            fileHash.write(fileByte)  

    def remove(self, fileHash):
        '''
        Remove file from the data tree
        '''
        pathHash = hash_to_path(fileHash)
        os.remove(pathHash)

    def show(self, fileHash):
        '''
        Show file in the data tree
        '''
        pathHash = hash_to_path(fileHash)
        with open(os.path.join(pathHash, fileHash), 'rb') as fileByte:
            return fileByte

