from django.core.cache import caches

redis_connection = caches["default"].client.get_client()


class RedisTestModelCache:

    hash_name = "RedisTestModel"

    @classmethod
    def get_key(cls, key):
        value = redis_connection.hget(cls.hash_name, key)
        if not value:
            cache = cls.set_cache()
            value = cache.get(key)
        return value

    @classmethod
    def set_cache(cls):
        from core.models import RedisTestModel
        values = RedisTestModel.objects.values("name", "id")

        cls.delete_cache()

        for item in values:
            redis_connection.hset(cls.hash_name, item["id"], item["name"])
        return values

    @classmethod
    def delete_cache(cls):
        redis_connection.delete(cls.hash_name)

    @classmethod
    def get_cache(cls):
        return redis_connection.hgetall(cls.hash_name) or cls.set_cache() or {}

    @classmethod
    def set_test_model_cache(cls, func):

        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            try:
                RedisTestModelCache.set_cache()
            except Exception as e:
                print(e)
            return value

        return wrapper


set_test_model_cache = RedisTestModelCache.set_test_model_cache