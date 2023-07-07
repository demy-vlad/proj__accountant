import requests
import os

def webhook_token() -> str:
    '''Use it to create new bot accounts and manage your existing bots.'''   
    # TOKEN = f"{os.getenv('TELEGRAM_BOT_TOKEN')}"
    TOKEN = "5492169980:AAGwRVcGhhHjue19Yxu2dRijlSyQjS31_ds"
    return TOKEN


def get_chat_id() -> list:
    '''Username of project participants'''
    chat_ids = ['717438486']
    return chat_ids


def send_message_bot(message):
    '''Sending messages project participants'''
    for chat_id in get_chat_id():
        requests.get('https://api.telegram.org/bot{}/sendMessage'.format(webhook_token()), params=dict(chat_id= chat_id,text=message, parse_mode= "HTML"))