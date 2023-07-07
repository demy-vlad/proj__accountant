from bs4 import BeautifulSoup
import requests
from loguru import logger
# from search.web_scraping.config import get_random_random_proxy, get_random_user_agent

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from proxy_list import ProxyList

def get_random_user_agent() -> str:
    '''Возвращает рандомный юзер агент'''
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    return user_agent_rotator.get_random_user_agent()

def get_random_random_proxy() -> str:
    '''Возвращает рандомный IP'''
    proxies = ProxyList()
    proxies.get_random_proxy()
    return proxies.get_random_proxy()



URL = "https://test.cryptoswift.net/invoice/f4a7dd3a-add2-4f1f-9286-c20a9588d21e"

def get_requests_html_text() -> list:
    ''' Парсим страницу. На выходе получаем HTML страницу '''
    header = {'User-Agent': get_random_user_agent()}
    logger.info(f'get_random_proxy: {get_random_random_proxy()}')
    logger.info(f'get_user_agent: {header}')

    get_html = requests.get(URL.format(headers=header))
    get_last_page_html(get_html, URL)

def get_last_page_html(get_html, url):
    """ Получаем кол. страниц """
    soup = BeautifulSoup(get_html.text, 'html.parser')
    print(soup)
    # last_page = soup.select('body > app-root > div > alliance-jobseeker-vacancies-root-page > div > alliance-jobseeker-desktop-vacancies-page > main > section > div > alliance-jobseeker-desktop-vacancies-list > div > div:nth-child(18) > alliance-vacancy-card-desktop > a')
    # logger.debug(soup)
    # add_number_to_url(last_page[0].text, url)

def add_number_to_url(last_page, url):
    """ Добавляем к ссылке номер страницы  """
    page = 1
    while page <= int(last_page):
        get_vacancies(f"{url}&page={page}")
        # print(f"{url}&page={page}")
        page = page + 1

def get_vacancies(page):
    """ Стягиваем вакансии из  """
    header = {'User-Agent': get_random_user_agent()}
    get_html = requests.get(page.format(headers=header))
    soup = BeautifulSoup(get_html.text, 'html.parser')
    last_page = soup.select('alliance-jobseeker-desktop-vacancies-list > div > div > alliance-vacancy-card-desktop > a')
    # Get the value of the "href" attribute
    for link in last_page:
        print(link.get('href'))
    print(page)


get_requests_html_text()