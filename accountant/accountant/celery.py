# celery.py

import os
import logging
from celery import Celery

# Установка переменной окружения для работы с Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accountant.settings')

# Создание объекта Celery
app = Celery('web_scraping')

# Загрузка конфигурации из настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач из приложений Django
app.autodiscover_tasks()

# Настройка логирования
logger = logging.getLogger('celery')
logger.setLevel(logging.INFO)

# celery -A accountant beat --scheduler django_celery_beat.schedulers:DatabaseScheduler --loglevel=info
# celery -A accountant worker --loglevel=info

