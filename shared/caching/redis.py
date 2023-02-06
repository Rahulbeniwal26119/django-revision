from django.core.cache import caches

redis_connection = caches["default"].client.connect()


def get_hash_key(hash_name, key):
    return redis_connection.hget(hash_name, key)


def set_hash_key(hash_name, key, value):
    redis_connection.hset(hash_name, key, value)
