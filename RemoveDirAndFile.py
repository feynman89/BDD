from os import *
from shutil import *


class RemoveDirAndFile(object):

    def __init__(self):
        pass

    def removeFile(self, file_path):
        remove(file_path)