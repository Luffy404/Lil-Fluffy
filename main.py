from textwrap import dedent

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


@client.listen()
async def on_ready():
    """Prints out some info about the bot once it's started and ready to use"""
    owner = (await client.application_info()).owner

    print(dedent(
        f"""
        I'm ready to go!
        Logged in as: {client.user}
        User ID: {client.user.id}
        Owner: {owner}
        """
    ))


client.run(TOKEN)
