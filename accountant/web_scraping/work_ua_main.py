from bs4 import BeautifulSoup
import requests
from loguru import logger
from web_scraping.config import get_random_random_proxy, get_random_user_agent
from .find_duplicates import *



def get_requests_html_text(URL) -> str:
    ''' Парсим страницу. На выходе получаем HTML страницу '''
    try:
        logger.info("[START SCRAPING] work.ua")
        header = {'User-Agent': get_random_user_agent()}
        response = requests.get(URL, headers=header)
        if response.status_code == 200:
            get_last_page_html(response, URL)
        else:
            print(f"Error while getting data. Response code: {response.status_code}")
    except requests.exceptions.RequestException as error:
        logger.error(f"The request failed: {error}")


def get_last_page_html(get_html, url):
    """ Получаем кол. страниц """
    try:
        soup = BeautifulSoup(get_html.text, 'html.parser')
        last_page = soup.select('ul.pagination.hidden-xs > li:nth-child(6) > a')
        add_number_to_url(last_page[0].text, url)
    except (IndexError, ValueError): add_number_to_url(5, url)

def add_number_to_url(last_page, url):
    """ Добавляем к ссылке номер страницы  """
    page = 1
    while page <= int(last_page):
        get_vacancies(f"{url}&page={page}")
        page = page + 1


def get_vacancies(page):
    """ Стягиваем вакансии из  """
    try:
        header = {'User-Agent': get_random_user_agent()}
        response = requests.get(page, headers=header)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            last_page = soup.select('#pjax-job-list >div > h2 > a')
            for link in last_page:
                find_duplicates(f"https://www.work.ua{link.get('href')}")
        else:
            print(f"Error while getting data. Response code: {response.status_code}")
    except requests.exceptions.RequestException as error:
        logger.error(f"The request failed: {error}")