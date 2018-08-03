'''
Split helpers function for the Tree library
'''

def hash_to_path(self, hashName=None):
    '''
    Convert hashName to directory path
    '''
    dirPath = ''.join([f'{symbol}/' if idx % 2 else f'{symbol}' for idx, symbol in enumerate(hashName)])[:-1]
    return dirPath
