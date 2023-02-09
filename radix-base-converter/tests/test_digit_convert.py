import pytest

from src.main import convert_radix_digit_to_int, char_position


def test_convert_a_to_decimal():
    assert convert_radix_digit_to_int("a", 16) == 10


def test_convert_5_base_6_to_decimal():
    assert convert_radix_digit_to_int("5", 6) == 5


def test_convert_3_base_2_to_decimal_fail():
    with pytest.raises(SystemExit):
        convert_radix_digit_to_int("3", 2)


def test_convert_non_alfanum_fail():
    with pytest.raises(SystemExit):
        convert_radix_digit_to_int("#", 2)


def test_position_of_a():
    assert char_position("a") == 0


def test_position_of_z():
    assert char_position("z") == 25
