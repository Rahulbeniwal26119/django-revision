import os
from celery import Celery
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_revision.settings")

app = Celery("django_revision")

# app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object('django_revision.celeryconfig', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
