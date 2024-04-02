# using fixture parameter



import pytest

@pytest.fixture(params=["sachin","123Sachin"])
def test1(request):
    print("test1 = ",request.param)



def test_teardown(test1):
    print("sucessfull ")
