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
import pytest


@pytest.mark.smoke
@pytest.mark.skip  # this will skip this test
def test_firstProgram3():
    msg = "Hello"
    assert msg == "Hi", "Test Failed because Hello not = Hi"


def test_credit_firstProgram4():
    a = 2
    b = 5
    assert a + 3 == 5, "Addition does not work!!"

# to create fixture, just like testNG @before test
# to open browser ,setting enviorment variables etc

@pytest.fixture()
def setup():
    print("I will be executing first")

def test_fixtureDemo(setup):
    print("I will execute step in fixtureDemo method")







