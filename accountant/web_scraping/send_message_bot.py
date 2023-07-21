import sqlite3
from loguru import logger
import requests

def read_from_telegramconfig():
    try:
        # Connect to the database
        conn = sqlite3.connect('db.sqlite3')
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        # Execute a SELECT query to retrieve data from a table
        cursor.execute('SELECT * FROM main_telegramconfig')
        # Retrieve the results as a list of tuples
        results = cursor.fetchall()
        # Close the database connection
        conn.close()
        # Return the results
        return results
        
    except sqlite3.Error as error:
        logger.error(f"Error while connecting to or reading from database: {error}")


def send_message_bot(message):
    '''Sending messages project participants'''
    telegramconfig = read_from_telegramconfig()
    TOKEN = telegramconfig[0][2]
    chat_id = telegramconfig[0][1]
    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN), 
                params=dict(chat_id= chat_id,text=message, parse_mode= "HTML"))