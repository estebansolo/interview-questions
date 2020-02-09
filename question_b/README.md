# Version Comparison

You can use this tool to compare 2 versions in order to know if is greater, lesser or equal to the other.

## Installation

`pip install version-comparison`

### Usage

- `get_lesser()` function return the lesser version of the provided, if none is lesser, the result is a `None` value.

- `get_greater()` function return the greater version of the provided, if none is greater, the result is a `None` value.

- `compare()` function return which one is greater, lesser or equal to the other.

```python
from versions_comparison import Comparison

versions = Comparison(version_1, version_2)
versions.get_lesser()
versions.get_greater()
versions.compare() 
```

### Valid Formats

- `dot numbers`: You can use numbers like `1.5`, `0.1.9`, `8.6.3`
- `chars`: You can validate a version with chars. `b > a` or `d < z`

### Exceptions

There are a coulpe of exceptions that could be used to catch possible errors throwed by the library.

- `FormatVersion`: This exception is thrown when the version provided does not have a valid format.
- `StringFormat`: This exception is thrown when the version provided is not a valid string type.

```python
from versions_comparison.exceptions import FormatVersion, StringFormat
```