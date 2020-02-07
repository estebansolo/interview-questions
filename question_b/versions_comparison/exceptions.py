"""
Set of exceptions to use with the module
"""


class FormatVersion(Exception):
    def __init__(self, message=None):
        """
        Initialize general error exception
        """

        if not message:
            message = "Versions Format must be the same."

        Exception.__init__(self, message)

class StringFormat(Exception):
    def __init__(self, message=None):
        """
        Initialize general error exception
        """

        if not message:
            message = "Provided versions must be in string format."

        Exception.__init__(self, message)