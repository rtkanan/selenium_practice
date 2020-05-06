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
def msetUp():
    print("Execute before each module")
    yield 
    print("Execute after each module")