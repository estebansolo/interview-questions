from time import sleep

import pytest
import fakeredis
from mock import Mock

from lru_redis_cache import LRUCache


redis = None
def setup_function():
    global redis
    redis = fakeredis.FakeStrictRedis(decode_responses=True)
    
def test_getter_cache():
    cache = LRUCache()
    cache.set_connection(redis)

    assert cache.get("my_key") is None

def test_setter_getter_cache():
    cache = LRUCache()

    redis.flushdb()
    redis.dbsize = Mock()
    cache.set_connection(redis)

    cache.set("my_key", "my_value")
    assert cache.get("my_key") == "my_value"


def test_lru_redis_cache():
    cache = LRUCache(cache_size=2)
    
    redis.flushdb()
    redis.object = Mock(side_effect=[2, 5])
    cache.set_connection(redis)

    cache.set("my_key", "my_value")
    cache.set("my_key_2", "my_value_2")

    # Update idletime of the oldest cache
    cache.get("my_key")

    # Replace the oldest cache (my_key_2)
    cache.set("my_key_3", "my_value_3")

    assert cache.get("my_key_2") is None
