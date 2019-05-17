from behave import *
from os import *
from RemoveDirAndFile import RemoveDirAndFile

removeDirAndFile = None

# 1
@given("I have class RemoveDirAndFile")
def step_impl(context):
    RemoveDirAndFile()


@when("I create new class RemoveDirAndFile")
def step_impl(context):
    global removeDirAndFile
    removeDirAndFile = RemoveDirAndFile()


@then("I have created RemoveDirAndFile")
def step_impl(context):
    global removeDirAndFile
    assert removeDirAndFile is not None


# 2
file_path = "D:/test/tdd/one.txt"
@given("I have a file with a path <file_path>")
def step_impl(context):
    global file_path
    my_file = open(file_path, O_CREAT)
    close(my_file)


@when("I call method with param <file_path> which remove file")
def step_impl(context):
    global removeDirAndFile, file_path
    removeDirAndFile.removeFile(file_path)


@then("File with a path <file_path> was remove")
def step_impl(context):
    global removeDirAndFile, file_path
    assert path.exists(file_path) is False


# 3
dir_path = "D:/test/tdd/hfolder"
@given("I have a dir with a path <dir_path>")
def step_impl(context):
    global dir_path
    if path.exists(dir_path) is False:
        mkdir(dir_path)


@when("I call method with param <dir_path> which remove dir")
def step_impl(context):
    global removeDirAndFile, dir_path
    removeDirAndFile.removeDir(dir_path)


@then("Dir with a path <dir_path> was remove")
def step_impl(context):
    global removeDirAndFile, dir_path
    assert path.exists(dir_path) is False

