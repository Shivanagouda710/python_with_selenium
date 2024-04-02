# using parametrize 


import pytest


@pytest.mark.parametrize("a , b ,final",[(1,2,3),(2,2,4),(2,2,3)])
def testAdd(a,b,final):
    assert a+b == final