from django.db import models
from shared.caching.redis import get_hash_key, set_hash_key
import json

# Create your models here.


class RedisTestModel(models.Model):
    created_dtm = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)

    model_cache_config = {
        "hash_key": "RedisTestModel",
        "hash_name": "hash_value"
    }

    class Meta:
        db_table = 'redis_test_model'

    @classmethod
    def get_cached(cls):
        return get_hash_key(RedisTestModel.model_cache_config["hash_name"],
                            RedisTestModel.model_cache_config["hash_key"])

    def save(self, *args, **kwargs):
        # update the redis cache
        super(RedisTestModel, self).save(*args, **kwargs)

        values = json.dumps(list(RedisTestModel.objects.values("name")))

        try:
            set_hash_key(RedisTestModel.model_cache_config["hash_name"],
                         RedisTestModel.model_cache_config["hash_key"], values)
        except:
            # silent the except lets play safe 
            pass