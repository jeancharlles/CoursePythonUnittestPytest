# TODO: Add imports
import time

import pytest

import module_02.cg00_apps.magic as mg


# TODO: Test get_a_number method
def test_magic_get_a_number_1():
    time.sleep(1)
    result = mg.get_a_number()
    assert result < 30


# TODO: Test get_a_number method
def test_magic_get_a_number_2():
    time.sleep(1)
    result = mg.get_a_number()
    assert result > 10


# TODO: Test get_double method
def test_magic_get_double():
    time.sleep(1)
    result = mg.get_double(25)
    assert result > 25


# TODO: Test get_double method
def test_magic_get_double():
    time.sleep(1)
    result = mg.get_a_list("Dog", "Cat", "Chicken", "Rabbit")
    assert result == ["Dog", "Cat", "Chicken", "Rabbit"]
