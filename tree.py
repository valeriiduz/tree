import os
import sys
import hashlib
import random

class Tree:

    pathToTree = os.path.dirname(os.path.abspath(__file__))
    
    def insert(self):
        '''
        Insert file to the data tree
        '''
        hashDir = hashName = hashlib.sha256(bytes(int(random.random()*100000))).hexdigest()
        for i in range(0, 98, 3): hashDir = hashDir[:i] + '/' + hashDir[i:]
        dirPath = self.pathToTree + hashDir
        print(dirPath)
        os.makedirs(dirPath)
        output = open(os.path.join(dirPath, hashName), 'wb')

    def rewrite(self, pathFile, fileName):
        '''
        Rewrite file in the data tree
        '''
        pas

    def remove(self, pathFile):
        '''
        Remove file from the data tree
        '''
        os.remove(pathFile)

    def show(self, pathFile):
        '''
        Show file in the data tree
        '''
        print(pathFile)

tr = Tree()
tr.insert()
