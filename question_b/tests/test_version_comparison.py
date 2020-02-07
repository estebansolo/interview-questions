import pytest
from versions_comparison import Comparison
from versions_comparison.exceptions import StringFormat, FormatVersion

string_formats = [
    ("1.1.7", []),
    ("0.25.9", None),
    (123, "ABC"),
]
    
@pytest.mark.parametrize("version_one,version_two", string_formats)
def test_validate_string_formats(version_one, version_two):
    with pytest.raises(StringFormat) as err:
        Comparison(version_one, version_two)

different_formats = [
    ("1.1.7", "Abc"),
    ("0.25.9", "abcd"),
    ("AFG", "1.2.3"),
]

@pytest.mark.parametrize("version_one,version_two", different_formats)
def test_validate_different_formats(version_one, version_two):
    with pytest.raises(FormatVersion) as err:
        Comparison(version_one, version_two)


lesser_version = [
    ("1.1.7", "1.2.5"),
    ("0.5.9", "0.6.0"),
    ("adf", "AFG"),
]

@pytest.mark.parametrize("version_one,version_two", lesser_version)
def test_validate_get_lesser(version_one, version_two):
    versions = Comparison(version_one, version_two)
    assert versions.get_lesser() == version_one

greater_version = [
    ("1.1.7", "1.2.5"),
    ("0.5.9", "0.6.0"),
    ("adf", "AFG"),
]

@pytest.mark.parametrize("version_one,version_two", greater_version)
def test_validate_get_greater(version_one, version_two):
    versions = Comparison(version_one, version_two)
    assert versions.get_greater() == version_two.lower()


compare_version = [
    ("1.1.7", "1.2.5", "version 1.1.7 is less than 1.2.5."),
    ("0.5.9", "0.5.9", "version 0.5.9 is equal to 0.5.9."),
    ("adf", "AFG", "version adf is less than afg."),
    ("astd", "AstD", "version astd is equal to astd."),
    ("9.0.0", "1.4.5", "version 9.0.0 is greater than 1.4.5."),
]

@pytest.mark.parametrize("version_one,version_two,expected", compare_version)
def test_validate_compare(version_one, version_two, expected):
    versions = Comparison(version_one, version_two)
    assert versions.compare() == expected