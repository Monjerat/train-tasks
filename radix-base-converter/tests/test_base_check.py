import pytest

from src.main import base_check


def test_base_left_border():
    assert base_check("2") == 2


def test_base_right_border():
    assert base_check("36") == 36


def test_base_out_of_border():
    with pytest.raises(ValueError):
        base_check("1010")
