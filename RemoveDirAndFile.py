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
        
    def checkExistFileOrDir(self, file_path):
        return path.exists(file_path)


if __name__ == '__main__':
    r = RemoveDirAndFile()

    while True:
        print("Введите, что удалить файл или каталог: ")
        variant = input()

        if variant == "файл" or variant == "Файл":
            print("Введите путь до файла: ")
            file_path = input()
            if r.checkExistFileOrDir(file_path):
                r.fillFile(file_path, "00000000000000000000000000000000000000000000")
                r.removeFile(file_path)
                if r.checkExistFileOrDir(file_path):
                    print("Не удалось удалить файл " + file_path)
                else:
                    print("Файл " + file_path + " был успешно удален")
            else:
                print("Такого файла не существует")
                continue
        elif variant == "папка" or variant == "Папка":
            print("Введите путь до папки: ")
            dir_path = input()
            if r.checkExistFileOrDir(dir_path):
                r.removeDir(dir_path)
                if r.checkExistFileOrDir(dir_path):
                    print("Не удалось удалить папку " + dir_path)
                else:
                    print("Папка " + dir_path + " был успешно удален")
            else:
                print("Такого каталога не существует")
                continue
        else:
            break
