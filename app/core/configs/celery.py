from celery import Celery

from app.core.configs import settings


celery = Celery(
    "tasks",
    broker=settings.REDIS_URL,
    include=["app.tasks.neural_network"],
)
