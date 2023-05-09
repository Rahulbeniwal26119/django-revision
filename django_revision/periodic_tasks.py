from celery.schedules import crontab


CELERY_BEAT_SCHEDULE = {
    'greet_user': {
        'task': 'django_revision.tasks.greet_user',
        'schedule': crontab(minute='*/1')
    }
}
