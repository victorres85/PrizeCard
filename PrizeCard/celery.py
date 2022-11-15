from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PrizeCard.settings')

app = Celery('PrizeCard', broker_url='redis://127.0.0.1:6379')

app.conf.enable_utc = False
app.conf.update(timezone = 'Europe/London')

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')