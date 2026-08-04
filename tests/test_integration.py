from roman.converter import add_roman, is_valid_roman


def test_add_roman_result_matches_spec_and_is_canonical():
    result = add_roman("II", "II")
    assert result == "IV"
    assert is_valid_roman(result) is True
