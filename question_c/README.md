# LRU Cache

This is a simple Least Recently Used (LRU) Cache with expiration time that use redis to store the data.

## Installation


## Usage

Import `LRUCache` from the lru_cache module, when creating an instance of this class you could pass:

- `cache_size`: Max size of the cache, the default value is 10
- `ttl`: Max time to expire the cache, the default value is 60 seconds
- `redis_host`: Host where the redis instance is allocated, default is localhost
- `redis_port`: Redis port, default is 6379

This class has three public methods to manage the cache:


- `set(name, value)` this function set a new cache value or replace the previous.

- `get(name)` this function return the cache element if it is stores, otherwise it will return a `None` value.

- `set_connection(RedisConnection)` this function allows you to set the redis instance to be used.

```python
from lru_cache import LRUCache

cache = LRUCache(cache_size=5, ttl=60)

cache.set("my_key", "my_value")
cache.get("my_key")

# Output
"my_value"
```

## Tests

In order to run the test cases you need to install the basic requirements from `requirements.txt` by running the following command.

`pip install -r requirements.txt`

Then, you need to run

`python -m pytest`

## Information

[LRU Cache Implementation](https://www.geeksforgeeks.org/lru-cache-implementation/)
