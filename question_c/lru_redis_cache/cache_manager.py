import json
from lru_redis_cache.redis_manager import RedisManager 


class LRUCache:
    def __init__(self, **kwargs):
        """
        Valid Arguments

        cache_size: Max size of the cache. Default 10
        ttl: Max time to expire the cache. Default 60 seconds
        redis_host: localhost
        redis_port: 6379
        """

        self._validate_args(kwargs)
        self._redis_manager = RedisManager(ttl=self.ttl, **self.redis_conn)

    def get(self, name):
        return self._redis_manager.get(name)

    def set(self, name, value):
        cached = self.get(name)
        actual_cache_size = self._redis_manager.db_size()
        
        if cached is None and self.cache_size == actual_cache_size:
            old_cache = self._get_older_cache()
            self._redis_manager.delete(old_cache)

        if isinstance(value, (list, dict)):
            value = json.dumps(value)

        self._redis_manager.set(name, value)

        return self._redis_manager.get(name)

    def set_connection(self, redis_connection):
        self._redis_manager.set_connection(redis_connection)

    def _get_older_cache(self):
        name = ""
        cache_list = self._redis_manager.get_all()
        if cache_list:
            idltime, name = sorted(cache_list, reverse=True)[0]
        
        return name

    def _validate_args(self, args):
        if not isinstance(args, dict):
            args = {}

        self.ttl = int(args.get("ttl") or 60)
        self.cache_size = int(args.get("cache_size") or 10)
        
        self.redis_conn = {
            "host": args.get("host") or "localhost",
            "port": args.get("port") or 6379
        }
