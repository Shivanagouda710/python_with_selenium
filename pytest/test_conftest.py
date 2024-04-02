# this will contain common functionality 

# To import these functtion in test_fixture etiher use autouse=True in conftest file or
#  write import statement in test fixtures so that it can access

import pytest

@pytest.fixture(autouse=True)
def setup():
    print("Launch browser")
    print("login")
    print("Browse products")
    yield
    print("log off")
    print("close browser")