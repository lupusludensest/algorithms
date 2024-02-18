# fixture dt 26 nov 2023
# used for pre requisites in testing
# correlation with the conftest.py

import pytest

@pytest.fixture
def my_fixture():
    return 10

@pytest.fixture
def my_other_fixture():
    return "Hello world!"


def test_my_functions(my_fixture, my_other_fixture):
    assert my_fixture == 10
    assert my_other_fixture == "Hello world!"

def test_my_fixture(my_fixture):
    assert my_fixture == 10

def test_my_other_fixture(my_other_fixture):
    return "Hello world!"
