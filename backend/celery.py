# import os
# from celery import Celery

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

# app = Celery("backend")
# app.config_from_object("django.conf:settings", namespace="CELERY")
# app.autodiscover_tasks()


# backend/celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')

# Use Redis as broker and backend
app.conf.broker_url = 'redis://127.0.0.1:6379/0'
app.conf.result_backend = 'redis://127.0.0.1:6379/1'

# Optional config
app.conf.task_serializer = 'json'
app.conf.result_serializer = 'json'
app.conf.accept_content = ['json']

app.autodiscover_tasks()
