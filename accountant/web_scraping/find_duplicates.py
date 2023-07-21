from loguru import logger
from web_scraping.config import get_current_date, get_formatted_time
from web_scraping.connect_to_database import add_to_database
from web_scraping.connect_to_database import read_from_main_parserresult


def find_duplicates(search_url ,arr_urls=None):
    """ Checking for duplicates in tables: main_parserresult """
    parserresult = read_from_main_parserresult()
    arr_urls = []
    for i in parserresult:
        arr_urls.append(i[3])
    
    if search_url not in arr_urls:
        logger.info(f'New entry added "{search_url}"')
        add_to_database(
            get_current_date(),
            get_formatted_time(),
            search_url,
            False,
        )