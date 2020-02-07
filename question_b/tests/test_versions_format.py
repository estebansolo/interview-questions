import pytest
from versions_comparison import VersionValidation
from versions_comparison.exceptions import FormatVersion

valid_versions = [
    ("1.1.7", "dot_numbers"),
    ("0.25.9", "dot_numbers"),
    ("Abc", "chars"),
]

invalid_version_format = [
    ("b2"),
    ("1.6.a"),
]
    
@pytest.mark.parametrize("version,expected", valid_versions)
def test_valid_version_format(version, expected):
    """ Validate if a version is valid """
    is_valid = VersionValidation(version)
    assert is_valid.format == expected

@pytest.mark.parametrize("version", invalid_version_format)
def test_invalid_version_format(version):
    """ Validate invalid formats """
    
    with pytest.raises(FormatVersion) as err:
        VersionValidation(version)
