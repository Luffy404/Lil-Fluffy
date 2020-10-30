import discord
from discord.ext import commands

with open('token.secret')as file:
    TOKEN = file.read().strip()


def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefix = ['l!', 'L!', '.', 'll!', 'LL!', 'Ll!', 'lL!']

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefix)(bot, message)


client = commands.Bot(command_prefix=get_prefix)

client.run(TOKEN)
