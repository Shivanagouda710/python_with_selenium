import pytest

@pytest.fixture(scope="session")
def myfixture():
    print("Conftest fixture is called ")