import pytest

# setUp is imported from conftest.py automatically
def test_one(setUp, msetUp):    
    print ("Running first test case")

def test_two(setUp, msetUp):
    print ("Running second test case")