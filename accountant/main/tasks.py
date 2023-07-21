# tasks.py

import logging
import sqlite3
import os
from celery import shared_task
from celery import Celery
from loguru import logger

# Получение объекта логирования для текущей задачи
logger = logging.getLogger(__name__)
# app = Celery('tasks', broker='redis://localhost:6379/0')
app = Celery('tasks', broker='pyamqp://guest@localhost//')  # Укажите адрес вашего брокера сообщений


@shared_task
def run_web_scraping_app():
    '''Web scraping'''
    logger.info("[START] - web scraping")
    os.system("python3 -m web_scraping.app")


@shared_task
def run_senging_results():
    '''Sending messages project participants'''
    logger.info("[INFO] - Sending messages project participants")
    os.system("python3 -m web_scraping.sending_results")


@app.task
def update_to_database_parserresult(id, flag):
    try:
        # Connect to the SQLite database using a connection pool
        with sqlite3.connect('db.sqlite3') as conn:
            # Define the SQL statement to update the flag in the table
            sql = "UPDATE main_parserresult SET flag = ? WHERE id = ?"
            # Execute the SQL statement with the flag and id values as parameters
            conn.execute(sql, (flag, id))
    except sqlite3.Error as error:
        # Configure and use a logger to capture errors
        logger.error(f'Failed to insert data into sqlite table {error}')


# Определение функции задачи для Celery
@app.task
def query_parserresult_by_flag(flag):
    try:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        # Выполнение запроса
        cursor.execute("SELECT * FROM main_parserresult WHERE flag = ?", (flag,))
        # Получение результатов
        results = cursor.fetchall()
        # Закрытие курсора и соединения
        cursor.close()
        conn.close()
        return results
    except sqlite3.Error as error:
        # Журналирование ошибки
        logger.error(f'Failed to query data from sqlite table {error}')