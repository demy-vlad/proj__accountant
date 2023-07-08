from accountant.main.web_scraping.connect_to_database import query_parserresult_by_flag, update_to_database_parserresult
from accountant.main.web_scraping.connect_to_database import update_to_database_parserresult
from send_message_bot import send_message_bot
from loguru import logger
import time

def senging_results():
    """
    1) филтруем результат по флагу
    2) добавляем таймер на отправку
    3) отправляем в телегу
    """
    data = query_parserresult_by_flag(False)
    for value in data:
        send_message_bot(value[3])
        update_to_database_parserresult(value[0], True)
        time.sleep(2)
    logger.debug(f"[SEND MESSAGE] Successful")

senging_results()