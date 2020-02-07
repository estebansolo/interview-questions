import re
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

        elif self.version_one > self.version_two:
            return self._response_format("is greater than")
        
        return self._response_format("is less than")

    def get_greater(self):
        if self.version_one == self.version_two:
            return None

        return max(self.version_one, self.version_two)
        
    def get_lesser(self):
        if self.version_one == self.version_two:
            return None
        
        return min(self.version_one, self.version_two)
    
    def _versions_validate(self):
        if self.version_one.format != self.version_two.format:
            raise FormatVersion

    def _response_format(self, comparison_type):
        return "version {} {} {}.".format(
            self.version_one,
            comparison_type,
            self.version_two
        )



class VersionValidation:
    expressions = {
        "chars": r"^[a-zA-Z]+$",
        "dot_numbers": r"^\d(\d|\.)+\d$"
    }
    
    def __init__(self, version):
        self.version = version.lower()
        self.format = None

        self._validate_format()

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

    def __lt__(self, version_cls):
        return self.version < version_cls.version

    def __gt__(self, version_cls):
        return self.version > version_cls.version

    def __ne__(self, version_cls):
        return self.version != version_cls.version

    def __eq__(self, version_cls):
        return self.version == version_cls

    def __str__(self):
        return self.version

    def __repr__(self):
        return self.version