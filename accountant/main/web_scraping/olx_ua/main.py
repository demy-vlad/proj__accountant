from bs4 import BeautifulSoup
import requests
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from proxy_list import ProxyList
import requests
import time
import random
import string


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


def get_requests_html_text() -> list:
    ''' Парсим страницу. На выходе получаем HTML страницу '''
    header = {'User-Agent': get_random_user_agent()}
    URL = f"https://img001.prntscr.com/file/img001/{random_string()}.png"
    get_html = requests.get(URL.format(headers=header))
    if get_html.status_code == 200:
        print("ok")
        send_message_bot(URL)

def random_string():
    """ Получаем кол. страниц """

    characters = string.ascii_letters + string.digits
    length = 20

    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def webhook_token() -> str:
    '''Use it to create new bot accounts and manage your existing bots.'''   
    # TOKEN = f"{os.getenv('TELEGRAM_BOT_TOKEN')}"
    TOKEN = "1336632599:AAFVh-LQFwJy22LJVqx1d-9bZ9WJQUVAvlk"
    return TOKEN


def get_chat_id() -> list:
    '''Username of project participants'''
    chat_ids = ['717438486']
    return chat_ids


def send_message_bot(message):
    '''Sending messages project participants'''
    for chat_id in get_chat_id():
        requests.get('https://api.telegram.org/bot{}/sendMessage'.format(webhook_token()), params=dict(chat_id= chat_id,text=message, parse_mode= "HTML"))


while True:
    time.sleep(2)
    get_requests_html_text()