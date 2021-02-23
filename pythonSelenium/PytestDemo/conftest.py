# while defining a Fixture to all the classes it is always mandatory to create a
# class called "conftest.py" so that it will call all the test_ methods in every file in runtime
# there is no need to define fixtures every where
# if we want to make them run only once before starting and after ending we use 'scope="class"'
# so it will run pre requisites once and the final after test once after all execution
# eg browser invoke

import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")  # eg to instantiate the browser in real time, Any prerequisites
    yield
    print("I will be executed last")  # eg to close the browsers/ delete the cookies at the end in real time


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]


# For parametrisation , use request instance only when fixtures with values are available
@pytest.fixture(params=[("chrome", "Amit"), ("Firefox", "Chandran"), ("IE", "winner")])
def crossBrowser(request):
    return request.param