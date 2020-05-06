import pytest

# setUp is imported from conftest.py automatically
def test_one(msetUp, setUp):    
    print ("Running first test case")

def test_two(msetUp, setUp):
    print ("Running second test case")