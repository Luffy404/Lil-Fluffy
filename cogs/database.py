import sqlite3


def create_connection():
    return sqlite3.connect('bot.db')


def execute_command(command):
    database = create_connection()
    cursor = database.cursor()
    result = cursor.execute(command)
    database.commit()
    database.close()
    return result
