import sqlite3
import traceback

from logs import log


def create_db():
    log('create sqlite')
    connection = sqlite3.connect('database/all_school.db')
    with open('database/all_school_sqlite.sql', 'r') as f:
        sql_commands = f.read()
    try:
        cursor = connection.cursor()
        cursor.executescript(sql_commands)
    except Exception as e:
        log(traceback.format_exc())
        log(repr(e))
    finally:
        connection.commit()
        connection.close()
        log('create sqlite finish')