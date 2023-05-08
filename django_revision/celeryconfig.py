# using rabbitmq as the broker
broker_url = "amqp://guest:guest@localhost:5672//"

# We can either set Redis, RabbitMQ, Postgresql, MySQL, MongoDB
# or other databases as the result backend.
# using mongodb as the result backend

# result_backend -> Use to store the results of tasks executed by celery

celery_mongodb_backend_settings = {
    "database": "django-revision-celery-log",
    "taskmeta_collection": "celery-task-meta",
    "user": "django",
    "password": "celery-broker",
    "host": "localhost",
    "port": 27017
}

# User pickle for complex data structures while passing arguments to tasks
# json, yaml, msgpack are other options.
task_serializer = "pickle"

timezone = "Asia/Kolkata"

# celery caches the results of tasks, so that if the same task is called again
# it can return the cached result instead of re-executing the task.
# By Default celery uses the Django cache backend
# using database redis 2 as the cache backend

cache_backend = "redis://localhost:6379/2"

# Either define imports here or set autodiscover_tasks either one is enough
imports = ("django_revision.tasks",)

# celery will stop accepting pickled content so need to allow pickle for deserialization
accept_content = ["pickle"]
