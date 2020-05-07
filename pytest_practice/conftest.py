import pytest

# This decorator is used mark the function as a fixture.
# @pytest.yield_fixture() # Works in all the versions
@pytest.fixture() # Syntax after pytest version 2.10
def setUp():
    print("Execute before each test case")
    yield 
    print("Execute after each test case")

# Define the fixture scope to each module rather than each function.
@pytest.fixture(scope="module")
def msetUp(browser, ostype):
    print("Browser: ", browser)
    print("Operating System: ", ostype)
    print("Execute before each module")
    yield 
    print("Execute after each module")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--ostype", help="Type of Operating System")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
    
@pytest.fixture(scope="session")
def ostype(request):
    return request.config.getoption("--ostype")