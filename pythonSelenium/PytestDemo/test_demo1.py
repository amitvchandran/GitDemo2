# 3 golden rules while using PYTEST
# Any pytest file should start with "test_xxx" or end with "_test"
# pytest method names should start with "test"
# any codes should be wrapped in methods only
# there should be different method names for same test

###################################################
# FOR GROUPING
# --------------- #
# if you have to run smoke test we should group it , we have to import pytest
# ... and we have to mark as smoke(any name)
# inorder to run in CMD give the command "py.test -m smoke  -v -s" ENTER (m stands for smoke)
# you can mark with this tag @pytest.mark.smoke (ONLY USE THIS FOR SMOKE AND REGRESSION)

#####################################################
# how to skip a Test
# use the tag @pytest.mark.skip (only to skip any one of the methods)
# if we want to fail a TC and not show inside the results then use @pytest.mark.xfail
# fixtures are used as setup and tear down methods for Test cases
# conftest file to generalise fixture and make it available to all test cases
# data driven and parametrisation can be done in written statements in tuple formats
# when u define fixture scope to class only, it will run once before class is initiated and at the end

###################################################
# to run in CMD
# -------------- #
# CD (change directory) to the file path
# then give command "py.test" ENTER
# to get more information "py.test -v" ENTER
# to get the entire console logs "py.test -v -s"
# to run in CMD for just one file give the specific file name "py.test test_demo2.py -v -s" ENTER
# To run all credit test in the complete directory give "py.test -k credit  -v -s" ENTER,
# which will run program 2 and program 4
# -k = method name execution
# -s = logs in out put
# -v = more info (metadata)
# To install pytest-html in CMD give command "pip install pytest-html"
# Then run your tests with: "--html=report.html"

#######################################################
import pytest


@pytest.mark.smoke
def test_firstProgram1():
    print("hello")


def test_credit_firstProgram2():
    print("Good Morning")


def test_crossBrowser1(crossBrowser):
    print(crossBrowser[1])


