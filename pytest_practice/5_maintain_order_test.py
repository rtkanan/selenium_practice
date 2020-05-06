import pytest

@pytest.mark.run(order=3)
def test_one(msetUp, setUp):  
    print ("Running test_one")

def test_two(msetUp, setUp):
    print ("Running test_two")

@pytest.mark.run(order=1)
def test_three(msetUp, setUp):
    print ("Running test_three")

def test_four(msetUp, setUp):
    print ("Running test_four")

@pytest.mark.run(order=2)
def test_five(msetUp, setUp):    
    print ("Running test_five")

def test_six(msetUp, setUp):
    print ("Running test_six")
