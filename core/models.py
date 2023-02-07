from django.db import models
from django.db.models.query import QuerySet
from core.utils.model_caching import set_test_model_cache


class RedisTestQuerySet(QuerySet):

    @set_test_model_cache
    def update(self, **kwargs):
        return super().update(**kwargs)

    @set_test_model_cache
    def all(self):
        return super().all()

    @set_test_model_cache
    def delete(self):
        return super().delete()


class RedisTestModel(models.Model):
    objects = RedisTestQuerySet.as_manager()

    created_dtm = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'redis_test_model'

    @set_test_model_cache
    def save(self, *args, **kwargs):
        # update the redis cache
        return super().save(*args, **kwargs)

    # mixins use instance methods
    @set_test_model_cache
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)
