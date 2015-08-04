import redis
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.encoding import force_text
from django.contrib.sessions.backends.base import CreateError

class RedisBackend:

    def __init__(self):
        host = settings.REDIS_HOST
        port = settings.REDIS_PORT

        if host is not None and port is not None:
            pool = redis.ConnectionPool(host=host, port=port, db=0)
            self.connection = redis.Redis(connection_pool=pool)
        else:
            raise ImproperlyConfigured("REDIS_HOST and REDIS_PORT not configured in settings")

    def get_ttl(self, key):
        return self.connection.ttl(key)

    def get_keys_matching(self, pattern):
        return self.connection.keys(pattern)

    def get(self, key):
        return force_text(self.connection.get(key))

    def exists(self, key):
        return self.connection.exists(key)

    def delete(self, key):
        return self.connection.delete(key)

    def save(self, key, expire, data, must_create):
        expire = int(expire)
        data = force_text(data)

        if must_create:
            if self.connection.setnx(key, data):
                self.connection.expire(key, expire)
            else:
                raise CreateError
        else:
            self.connection.setex(key, expire, data)
