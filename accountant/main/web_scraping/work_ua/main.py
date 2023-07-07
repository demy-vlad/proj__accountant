from bs4 import BeautifulSoup
import requests
from loguru import logger
from accountant.main.web_scraping.config import get_random_random_proxy, get_random_user_agent
from ..find_duplicates import *


def get_requests_html_text(URL) -> str:
    ''' Парсим страницу. На выходе получаем HTML страницу '''
    logger.info("[START SCRAPING] work.ua")
    header = {'User-Agent': get_random_user_agent()}
    logger.info(f'get_random_proxy: {get_random_random_proxy()}')
    logger.info(f'get_user_agent: {header}')

    get_html = requests.get(URL.format(headers=header))
    get_last_page_html(get_html, URL)


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
    header = {'User-Agent': get_random_user_agent()}
    get_html = requests.get(page.format(headers=header))
    soup = BeautifulSoup(get_html.text, 'html.parser')
    last_page = soup.select('#pjax-job-list >div > h2 > a')
    # Get the value of the "href" attribute
    for link in last_page:
        find_duplicates(f"https://www.work.ua{link.get('href')}")