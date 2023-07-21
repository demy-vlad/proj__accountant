from bs4 import BeautifulSoup
import requests
from loguru import logger
from web_scraping.config import get_random_random_proxy, get_random_user_agent
from .find_duplicates import *

def get_requests_html_text(URL):
    ''' Парсим страницу. На выходе получаем HTML страницу '''
    try:
        header = {'User-Agent': get_random_user_agent()}
        proxies = get_random_random_proxy()
        logger.info(f"return: {header}")
        response = requests.get(URL, headers=header, proxies=proxies, timeout=10)

        if response.status_code == 200:
            get_last_page_html(response, URL)
        else:
            print(f"Ошибка при получении данных. Код ответа: {response.status_code}")
            get_requests_html_text(URL)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        get_requests_html_text(URL)



# def get_requests_html_text(URL) -> str:
#     ''' Парсим страницу. На выходе получаем HTML страницу '''
#     logger.info("[START SCRAPING] work.ua")
#     header = {'User-Agent': get_random_user_agent()}
#     logger.info(f'get_random_proxy: {get_random_random_proxy()}')
#     logger.info(f'get_user_agent: {header}')

#     get_html = requests.get(URL.format(headers=header))
#     logger.error(get_html)
#     get_last_page_html(get_html, URL)


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


# def get_vacancies(page):
#     """ Стягиваем вакансии из  """
#     header = {'User-Agent': get_random_user_agent()}
#     get_html = requests.get(page.format(headers=header))
#     soup = BeautifulSoup(get_html.text, 'html.parser')
#     last_page = soup.select('#pjax-job-list >div > h2 > a')
#     # Get the value of the "href" attribute
#     for link in last_page:
#         find_duplicates(f"https://www.work.ua{link.get('href')}")

def get_vacancies(page):
    """ Стягиваем вакансии из  """
    try:
        header = {'User-Agent': get_random_user_agent()}
        proxies = get_random_random_proxy()
        logger.info(f"return: {header}")
        response = requests.get(page, headers=header, proxies=proxies, timeout=10)
        if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                last_page = soup.select('#pjax-job-list >div > h2 > a')
                # Get the value of the "href" attribute
                for link in last_page:
                    find_duplicates(f"https://www.work.ua{link.get('href')}")
        else:
            print(f"Ошибка при получении данных. Код ответа: {response.status_code}")
            get_vacancies(page)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        get_vacancies(page)