from src.main import convert_to_decimal


def test_convert_aa_base_16_to_decimal():
    assert convert_to_decimal(16, "aa") == 170


def test_convert_negative_num_to_decimal():
    assert convert_to_decimal(14, "-b") == -11


def test_convert_rational_num_to_decimal():
    assert convert_to_decimal(16, "12.5") == 18.3125
