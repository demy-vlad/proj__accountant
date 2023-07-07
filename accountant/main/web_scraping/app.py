from accountant.main.web_scraping.connect_to_database import read_from_main_parserconfig
from accountant.main.web_scraping.work_ua.main import get_requests_html_text
from .find_duplicates import *


def read_from_database() -> list:
    """Вытаскиваем с БД все ссылки с настроек"""
    parserconfig = read_from_main_parserconfig()
    arr_urls = []
    for i in parserconfig:
        arr_urls.append(i[2])
    return arr_urls

def list_validation() -> str:
    """
    Валидируем список 
    и перенаправляем к нужному скраперу
    """
    for url in read_from_database():
        if url.startswith("https://www.work.ua/"):
            get_requests_html_text(url)

list_validation()