from src.main import convert_to_decimal


def test_convert_aa_base_16_to_decimal():
    assert convert_to_decimal(16, "aa") == 170
