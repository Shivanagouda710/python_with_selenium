import pytest

# Use the sanity marker in your tests
@pytest.mark.sanity
def test2():
    print('test2')



@pytest.mark.regression
def test3():
    print('test3')

@pytest.mark.skip
def test4():
    print('test4')

@pytest.mark.xfail
def test5():
    print('test5')
