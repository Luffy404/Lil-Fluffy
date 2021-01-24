from cogs.internal import database


def createDatabase(databaseName):
    database.execute_command('''CREATE TABLE "counter" (
                            "all_messages" INTEGER,
                            "all_commands" INTEGER,
                            "completed_commands" INTEGER,
                            "loc" INTEGER,
                            "highest_loc" INTEGER,
                            "chars_in_total" INTEGER,
                            "highest_chars_in_total" INTEGER
                            )''', databaseName)
    database.execute_command('''INSERT INTO "counter" VALUES(0, 0, 0, 0, 0, 0 , 0)''', databaseName)


createDatabase("bot.db")
