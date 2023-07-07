import sqlite3
from loguru import logger


def read_from_main_parserconfig():
    try:
        # Connect to the database
        conn = sqlite3.connect('accountant\db.sqlite3')
        
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        
        # Execute a SELECT query to retrieve data from a table
        cursor.execute('SELECT * FROM main_parserconfig')
        
        # Retrieve the results as a list of tuples
        results = cursor.fetchall()
        
        # Close the database connection
        conn.close()
        
        # Return the results
        return results
        
    except sqlite3.Error as error:
        logger.error(f"Error while connecting to or reading from database: {error}")


def read_from_main_parserresult():
    try:
        # Connect to the database
        conn = sqlite3.connect('accountant\db.sqlite3')
        
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        
        # Execute a SELECT query to retrieve data from a table
        cursor.execute('SELECT * FROM main_parserresult')
        
        # Retrieve the results as a list of tuples
        results = cursor.fetchall()
        
        # Close the database connection
        conn.close()
        
        # Return the results
        return results
        
    except sqlite3.Error as error:
        logger.error(f"Error while connecting to or reading from database: {error}")


def add_to_database(date, time, url):
    try:
        # Connect to the database
        conn = sqlite3.connect('accountant\db.sqlite3')
        
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        
        # Get the current maximum ID value from the table
        cursor.execute('SELECT MAX(id) FROM main_parserresult')
        max_id = cursor.fetchone()[0]
        if max_id is None:
            max_id = 0
        
        # Generate a new ID value
        new_id = max_id + 1
        
        # Execute an INSERT query to add new data to a table
        cursor.execute('INSERT INTO main_parserresult VALUES (?, ?, ?, ?)', (new_id, date, time, url))
        
        # Commit the changes to the database
        conn.commit()
        
        # Close the database connection
        conn.close()
        
    except sqlite3.Error as error:
        logger.error(f'Failed to insert data into sqlite table {error}')