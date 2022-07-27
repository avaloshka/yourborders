from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedule import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'borders.settings')

app = Celery('borders', broker='localhost:8000')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
	'every-60-seconds': {
		'task': 'website.belarus.get_border_info',
		'schedule': crontab(minutes='*/60'),
	}
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
	print('Request: {0!r}'.format(self.request))

