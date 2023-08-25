from celery import Celery
from src.config.settings import env

celery_app = Celery(
    "tasks",
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0",
    include=["src.tasks.images"],
)
broker_url: str = env.str("CELERY_BROKER_URL", "redis://127.0.0.1:6379/11")
result_backend: str = env.str("CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/12")
