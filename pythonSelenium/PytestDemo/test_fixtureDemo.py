
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

#######################################################
# to create fixture, just like testNG @before test
# to open browser ,setting environment variables etc
# tier down : to run something after the test case execution is done , Use "Yield" keyword
# basically pre setup/ prerequisite will be run before yield and post set up will run after yield for same "Fixture"
import pytest


@pytest.mark.usefixtures("setup")
class TestExample:


    def test_fixtureDemo1(self):
        print("I will execute step in fixtureDemo method")

    def test_fixtureDemo2(self):
        print("I will execute step in fixtureDemo method")


    def test_fixtureDemo3(self):
        print("I will execute step in fixtureDemo method")

    def test_fixtureDemo4(self):
        print("I will execute step in fixtureDemo method")
