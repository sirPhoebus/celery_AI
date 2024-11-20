import os
from celery import Celery

celery_app = Celery('crypto_trading',
                   broker='redis://localhost:6379/0',
                   backend='redis://localhost:6379/0',
                   include=['crypto_trading.tasks'])

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)