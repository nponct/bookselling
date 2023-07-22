import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "organizer.settings")
app = Celery("organizer")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule={
    'check-task-and-send-mail-everyhour':{
        'task':'regulator.tasks.send_mail_func',
        'schedule': crontab(minute=0,hour='*/3'),
    },
}