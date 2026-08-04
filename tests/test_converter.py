# test suite
from roman.converter import to_roman, from_roman


def test_one():
    assert to_roman(1) == "I"


def test_two():
    assert to_roman(2) == "II"


def test_three():
    assert to_roman(3) == "III"


def test_five():
    assert to_roman(5) == "V"


def test_ten():
    assert to_roman(10) == "X"


def test_fifty():
    assert to_roman(50) == "L"


def test_hundred():
    assert to_roman(100) == "C"


def test_five_hundred():
    assert to_roman(500) == "D"


def test_thousand():
    assert to_roman(1000) == "M"


def test_from_one():
    assert from_roman("I") == 1


def test_from_five():
    assert from_roman("V") == 5


def test_from_two():
    assert from_roman("II") == 2


def test_roundtrip_small():
    assert from_roman(to_roman(7)) == 7


def test_roundtrip_medium():
    assert from_roman(to_roman(58)) == 58


def test_lowercase_input():
    assert from_roman("xi") == 11

import pytest
from roman.converter import RomanError, is_valid_roman, add_roman, subtract_roman

def test_to_roman_rejects_non_int():
    with pytest.raises(RomanError):
        to_roman("4")


def test_to_roman_rejects_bool():
    with pytest.raises(RomanError):
        to_roman(True)


def test_to_roman_rejects_below_min():
    with pytest.raises(RomanError):
        to_roman(0)


def test_to_roman_rejects_above_max():
    with pytest.raises(RomanError):
        to_roman(4000)


def test_to_roman_upper_bound_ok():
    assert to_roman(3999) == "MMMCMXCIX"


def test_to_roman_nine():
    assert to_roman(9) == "IX"


def test_to_roman_forty_five():
    assert to_roman(45) == "XLV"


def test_from_roman_rejects_non_string():
    with pytest.raises(RomanError):
        from_roman(123)


def test_from_roman_rejects_empty_string():
    with pytest.raises(RomanError):
        from_roman("")


def test_from_roman_rejects_invalid_character():
    with pytest.raises(RomanError):
        from_roman("IIJ")


def test_from_roman_subtractive_pairs():
    assert from_roman("IX") == 9
    assert from_roman("XL") == 40
    assert from_roman("CM") == 900


def test_from_roman_rejects_invalid_subtractive_pair():
    with pytest.raises(RomanError):
        from_roman("IC")


def test_from_roman_rejects_out_of_range_total():
    with pytest.raises(RomanError):
        from_roman("MMMM")


def test_is_valid_roman_true():
    assert is_valid_roman("XII") is True


def test_is_valid_roman_false():
    assert is_valid_roman("IIJ") is False


def test_add_roman_basic():
    assert add_roman("I", "II") == "III"


def test_subtract_roman_basic():
    assert subtract_roman("V", "II") == "III"