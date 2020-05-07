import pytest

@pytest.mark.usefixtures("msetUp", "setUp") # This applies the passed fixtures to all the methods availabled in the class
class TestClassDemo():

    @pytest.fixture(autouse=True) # This enables to use the variable defined in the method to be accessible in the other methods of the class.
    def classSetup(self):
        self.var = 10
    
    def test_one(self):
        result = self.var + 5
        assert result == 15
    
    def test_two(self):
        result = self.var + 10
        assert result == 20