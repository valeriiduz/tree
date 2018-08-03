"""
Tree library

"""

import os
import sys
import random
import hashlib

class Tree:

    def __init__(self, pathToTree=None):

        if not pathToTree:
            self.pathToTree = os.path.dirname(os.path.abspath(__file__))
    
    def insert(self, fileByte):
        '''
        Insert file to the data tree
        '''
        hashName = hashlib.sha256(bytes(int(random.random()*100000))).hexdigest()
        hashDir = hash_to_path(hashName)
        dirPath = self.pathToTree + hashDir
        os.makedirs(dirPath)
        with open(os.path.join(dirPath, hashName), 'wb') as fileHash:
            fileHash.write(file_byte)

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

