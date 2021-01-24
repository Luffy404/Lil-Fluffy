import sqlite3


def create_connection(database):
    return sqlite3.connect(database)


def execute_command(command, database='bot.db'):
    database = create_connection(database)
    cursor = database.cursor()
    result = cursor.execute(command)
    database.commit()
    database.close()
    return result


def execute_command_fetchall(command, database='bot.db'):
    database = create_connection(database)
    cursor = database.cursor()
    result = cursor.execute(command)
    result = result.fetchall()
    database.commit()
    database.close()
    return result
