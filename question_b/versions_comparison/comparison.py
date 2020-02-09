import re
from versions_comparison.decorators import version_compare
from versions_comparison.exceptions import FormatVersion, StringFormat

class Comparison:
    def __init__(self, version_one: str, version_two: str):
        if not isinstance(version_one, str) or not isinstance(version_two, str):
            raise StringFormat

        self.version_one = VersionValidation(version_one)
        self.version_two = VersionValidation(version_two)

        self._versions_validate()

    def compare(self):
        if self.version_one == self.version_two:
            return self._response_format("is equal to")

        elif self._greater_than():
            return self._response_format("is greater than")
        
        return self._response_format("is less than")

    @version_compare
    def get_greater(self, first_greater=False):
        return self.version_one if first_greater else self.version_two
    
    @version_compare
    def get_lesser(self, first_greater=False):
        return self.version_one if not first_greater else self.version_two
    
    def _versions_validate(self):
        if self.version_one.format != self.version_two.format:
            raise FormatVersion

    def _response_format(self, comparison_type):
        return "version {} {} {}.".format(
            self.version_one,
            comparison_type,
            self.version_two
        )

    def _greater_than(self):
        version_format = self.version_one.format
        if version_format == "dot_numbers":
            return self._greater_number()

        version_one_len = self.version_one.length()
        version_two_len = self.version_two.length()

        if version_one_len != version_two_len:
            return version_one_len > version_two_len

        return str(self.version_one) > str(self.version_two)

    def _greater_number(self):
        v1_nums = str(self.version_one).split('.')
        v2_nums = str(self.version_two).split('.')

        for v1, v2 in zip(v1_nums, v2_nums):
            if int(v1) == int(v2):
                continue
            
            return int(v1) > int(v2)

        return str(self.version_one) > str(self.version_two)

class VersionValidation:
    expressions = {
        "chars": r"^[a-zA-Z]+$",
        "dot_numbers": r"^\d(\d|\.)+\d$"
    }
    
    def __init__(self, version):
        self.version = version.lower()
        self.format = None

        self._validate_format()

    def length(self):
        return len(self.version)

    def _validate_format(self):
        for name, expression in self.expressions.items():
            if self._is_valid_format(expression, self.version):
                self.format = name                    
                break
        else:
            names = " or ".join(self.expressions.keys())
            raise FormatVersion(f"The version must be {names} format.")

    @staticmethod
    def _is_valid_format(expression, string):
        return re.search(expression, string)

    def __eq__(self, version):
        return self.version == version

    def __str__(self):
        return self.version
        
    def __repr__(self):
        return self.version
        