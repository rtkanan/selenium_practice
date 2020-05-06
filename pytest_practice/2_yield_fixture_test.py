import pytest

# This decorator is used mark the function as a fixture.
# @pytest.yield_fixture() # Works in all the versions
@pytest.fixture() # Syntax after pytest version 2.10
def setUp():
    print("Execute before each test case")
    yield 
    print("Execute after each test case")

# Pass the fixture to function defenition to ensure the fixture function executes before the actual test
def test_one(setUp):    
    print ("Running first test case")

def test_two(setUp):
    print ("Running second test case")