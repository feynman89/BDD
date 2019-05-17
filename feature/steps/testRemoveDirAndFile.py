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

