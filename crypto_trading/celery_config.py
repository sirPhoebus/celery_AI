import os
from celery import Celery

# Use the Redis service name from docker-compose as the hostname
celery_app = Celery('crypto_trading',
                   broker='redis://redis:6379/0',
                   backend='redis://redis:6379/0',
                   include=['crypto_trading.tasks'])

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)