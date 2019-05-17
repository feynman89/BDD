from os import *
from shutil import *


class RemoveDirAndFile(object):

    def __init__(self):
        pass

    def removeFile(self, file_path):
        remove(file_path)

    def removeDir(self, dir_path):
        rmtree(dir_path)
        
    def fillFile(self, file_path, data):
        my_file = open(file_path, O_RDWR)
        write(my_file, data.encode())
        close(my_file)