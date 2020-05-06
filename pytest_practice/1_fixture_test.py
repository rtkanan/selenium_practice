import pytest

# This decorator is used mark the function as a fixture.
@pytest.fixture()
def setUp():
    print("Running Setup")

# Pass the fixture to function defenition to ensure the fixture function executes before the actual test
def test_one(setUp):    
    print ("Running first test case")

def test_two(setUp):
    print ("Running second test case")