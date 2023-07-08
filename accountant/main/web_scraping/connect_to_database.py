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


def add_to_database(date, time, url, flag):
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
        cursor.execute('INSERT INTO main_parserresult VALUES (?, ?, ?, ?, ?)', (new_id, date, time, url, flag))
        # Commit the changes to the database
        conn.commit()
        # Close the database connection
        conn.close()
        
    except sqlite3.Error as error:
        logger.error(f'Failed to insert data into sqlite table {error}')


def update_to_database_parserresult(id, flag):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('accountant/db.sqlite3')
        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        # Define the SQL statement to update the flag in the table
        sql = "UPDATE main_parserresult SET flag = ? WHERE id = ?"
        # Execute the SQL statement with the flag and id values as parameters
        cursor.execute(sql, (flag, id))
        # Commit the changes to the database
        conn.commit()
        # Close the cursor and the database connection
        cursor.close()
        conn.close()
    except sqlite3.Error as error:
        logger.error(f'Failed to insert data into sqlite table {error}')


def update_to_database_parserconfig(id, flag):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('accountant/db.sqlite3')
        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        # Define the SQL statement to update the flag in the table
        sql = "UPDATE main_parserconfig SET flag = ? WHERE id = ?"
        # Execute the SQL statement with the flag and id values as parameters
        cursor.execute(sql, (flag, id))
        # Commit the changes to the database
        conn.commit()
        # Close the cursor and the database connection
        cursor.close()
        conn.close()
    except sqlite3.Error as error:
        logger.error(f'Failed to insert data into sqlite table {error}')


def query_parserresult_by_flag(flag):
    try:
        conn = sqlite3.connect('accountant\db.sqlite3')
        cursor = conn.cursor()
        # Execute the query
        cursor.execute("SELECT * FROM main_parserresult WHERE flag = ?", (flag,))
        # Fetch all the results
        results = cursor.fetchall()
        # Close the cursor and connection
        cursor.close()
        conn.close()
        return results
    except sqlite3.Error as error:
        logger.error(f'Failed to insert data into sqlite table {error}')


def update_to_database_parserresult(id, flag):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('accountant/db.sqlite3')
        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        # Define the SQL statement to update the flag in the table
        sql = "UPDATE main_parserresult SET flag = ? WHERE id = ?"
        # Execute the SQL statement with the flag and id values as parameters
        cursor.execute(sql, (flag, id))
        # Commit the changes to the database
        conn.commit()
        # Close the cursor and the database connection
        cursor.close()
        conn.close()
    except sqlite3.Error as error:
        logger.error(f'Failed to insert data into sqlite table {error}')