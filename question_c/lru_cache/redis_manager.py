import redis


class RedisManager: 
    redis_connection = None

    def __init__(self, ttl=60, **kwargs):
        self.ttl = ttl
        self._redis_connection(**kwargs)
        
    def set(self, name, value):
        self.redis_connection.set(name, value, ex=self.ttl)

    def get(self, name):
        return self.redis_connection.get(name)

    def get_all(self):
        cursor = self.redis_connection.scan_iter()
        return [(self._get_idletime(key), key) for key in cursor]

    def delete(self, name):
        return self.redis_connection.delete(name)

    def db_size(self):
        return self.redis_connection.dbsize()

    def set_connection(self, connection):
        self.redis_connection = connection

    def _get_idletime(self, name):
        return self.redis_connection.object("idletime", name)

    def _redis_connection(self, **kwargs):
        if self.redis_connection is None:
            self.redis_connection = redis.StrictRedis(
                decode_responses=True,
                **kwargs
            )