import time
from .connect_to_database import query_parserresult_by_flag
from .send_message_bot import send_message_bot
from loguru import logger
from main.tasks import update_to_database_parserresult


def senging_results():
    """
    1) филтруем результат по флагу
    2) добавляем таймер на отправку
    3) отправляем в телегу
    """

    data = query_parserresult_by_flag(False)
    logger.debug(f"[data] - {data}")
    for value in data:
        send_message_bot(value[3])
        update_to_database_parserresult(value[0], True)
        time.sleep(2)
    logger.info(f"[SEND MESSAGE] Successful")

senging_results()