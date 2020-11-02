from datetime import datetime
import json
import logging
import os

from discord.ext import commands


with open('token.secret')as fp:
    TOKEN = fp.read().strip()
    fp.close()

with open('config.json') as file:
    config = json.load(file)
    DESCRIPTION = config["DESCRIPTION"]
    COGS = config["COGS"]
    LOG_AS_FILE = config["LOG_AS_FILE"]
    LOGFORMAT = config["LOGFORMAT"]
    DATEFORMAT = config["DATEFORMAT"]
    file.close()

log_formatter = logging.Formatter(LOGFORMAT, datefmt=DATEFORMAT)
root_logger = logging.getLogger()
root_logger.level = logging.INFO
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
root_logger.addHandler(console_handler)

if LOG_AS_FILE is True:
    try:
        now = datetime.now()
        os.replace('latest.log', f'logs\\{now.strftime("%d-%m-%Y %H-%M")}.log')

    except Exception as e:
        exc = f"{type(e).__name__}: {e}"
        root_logger.error(f'Failed to move latest.log appending!: {exc}')

    file_handler = logging.FileHandler('latest.log')
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)


def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefix = ['l!', 'L!', '.', 'll!', 'LL!', 'Ll!', 'lL!']

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefix)(bot, message)


client = commands.Bot(command_prefix=get_prefix, description=DESCRIPTION)


for cog in COGS:
    try:
        client.load_extension(cog)
        print(f"Loaded {cog}.")
    except Exception as e:
        exc = f"{type(e).__name__}: {e}"
        print(f"Failed to load Extension {cog}:\n{exc}")

client.run(TOKEN)
