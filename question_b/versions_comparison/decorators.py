
def version_compare(fn):
    def wrapper(self, **kwargs):
        if self.version_one == self.version_two:
            return None

        first_greater = self._greater_than()
        return fn(self, first_greater=first_greater)

    return wrapper