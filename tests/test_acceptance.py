from roman.converter import to_roman, from_roman, is_valid_roman


def test_criterion_1_subtractive_notation_is_mandatory():
    assert to_roman(4) == "IV"


def test_criterion_2_leading_and_trailing_whitespace_is_trimmed():
    assert from_roman("  IV  ") == 4


def test_criterion_3_non_canonical_strings_are_not_valid():
    assert is_valid_roman("IIII") is False
