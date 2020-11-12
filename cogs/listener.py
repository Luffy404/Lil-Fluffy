import json
import os
import pathlib
from pathlib import Path
from textwrap import dedent
import logging

import discord
from discord.ext import commands
from discord.ext.commands import Bot

from cogs.internal import database

with open(str(Path().parent.absolute()) + "\\config.json") as fp:
    config = json.load(fp)
    QUESTIONMARK = config["QUESTIONMARK"]
    LOG_MESSAGES = config["LOG_MESSAGES"]
    FILEFORMATS_TO_COUNT = config["FILEFORMATS_TO_COUNT"]
    fp.close()


class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Prints out some info about the bot once it's started and ready to use"""
        bot_app_info = (await Bot.application_info(self.bot))
        allfiles = [""]
        linesofcode = 0
        chars_in_total = 0
        highest_chars_in_total = database.execute_command_fetchall("SELECT highest_chars_in_total from counter")
        highest_loc = database.execute_command_fetchall("SELECT highest_loc from counter")
        for path, subdirs, files in os.walk(str(Path().parent.absolute())):
            for name in files:
                allfiles.append(str(pathlib.PurePath(path, name)))
        for file in allfiles:
            if file.endswith(tuple(FILEFORMATS_TO_COUNT)):
                currentfile = open(file, 'r')
                chars_in_total += len(currentfile.read())
                for _ in file:
                    linesofcode += 1

        if chars_in_total > highest_chars_in_total[0][0]:
            database.execute_command(f'UPDATE counter SET highest_chars_in_total = {chars_in_total}')
        database.execute_command(f'UPDATE counter SET chars_in_total = {chars_in_total}')

        if linesofcode > highest_loc[0][0]:
            database.execute_command(f'UPDATE counter SET highest_loc = {linesofcode}')
        database.execute_command(f'UPDATE counter SET loc = {linesofcode}')

        await self.bot.wait_until_ready()
        await self.bot.change_presence(
            activity=discord.Activity(name=' over .help for info', type=discord.ActivityType.watching))
        print(dedent(
            f"""
            Bot is ready and awaiting Commands!
            Logged in as: {bot_app_info.name}
            User ID: {bot_app_info.id}
            Owner: {bot_app_info.owner} ({bot_app_info.owner.id})
            """
        ))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You're not allowed to use this command!")
            logging.info(f'User "{ctx.message.author}" ({ctx.message.author.id}) '
                         f'tried to issue an command he had no permissions for!')
            logging.info(f'{ctx.message.author}: {ctx.message.content}')

        elif isinstance(error, commands.CommandNotFound):
            await ctx.message.add_reaction(QUESTIONMARK)
            logging.info(f'User "{ctx.message.author}" ({ctx.message.author.id}) '
                         f"tried to issue an command that didn't exist!")
            logging.info(f'{ctx.message.author}: {ctx.message.content}')

        elif isinstance(error, commands.NotOwner):
            await ctx.send("You're not the owner of the bot.")
            logging.info(f'User "{ctx.message.author}" ({ctx.message.author.id}) '
                         f"tried to issue an command that requires Owner privileges!")
            logging.info(f'{ctx.message.author}: {ctx.message.content}')

        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f"I don't have the required permission to execute this command.")
            logging.info(f'User "{ctx.message.author}" ({ctx.message.author.id}) '
                         f"tried to issue an command that the bot has no permission to execute!")
            logging.info(f'{ctx.message.author}: {ctx.message.content}')

        elif isinstance(error, commands.BadArgument):
            logging.info(f'User "{ctx.message.author}" ({ctx.message.author.id}) '
                         f"gave a bad argument!")
            logging.info(f'{ctx.message.author}: {ctx.message.content}')

        else:
            await ctx.send("An unexpected Error Occured, please Tag `Mad Luffy#3039`!")
            await ctx.send(f"```{error}```")
            logging.warning(f'User "{ctx.message.author}" ({ctx.message.author.id}) '
                            f"tried to invoke a command wich made an unexpected Error occur!")
            logging.warning(f'{ctx.message.author}: {ctx.message.content}')
            logging.warning(error)

    @commands.Cog.listener()
    async def on_command(self, message):
        database.execute_command('UPDATE counter SET all_commands = all_commands + 1')

    @commands.Cog.listener()
    async def on_command_completion(self, message):
        database.execute_command('UPDATE counter SET completed_commands = completed_commands + 1')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        logging.info("Succsessfully joined a server: " + guild.name)
        logging.info(f"Servers ({len(Bot(self.bot).guilds)}")
        for guild in Bot(self.bot).guilds:
            logging.info(guild.name)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        logging.info("I Left a server: " + guild.name)
        logging.info(f"Servers ({len(Bot(self.bot).guilds)}")
        for guild in Bot(self.bot).guilds:
            logging.info(guild.name)


def setup(bot):
    @bot.event
    async def on_message(message):
        if LOG_MESSAGES is True:
            # Probably a Violation of Discord ToS yet I keep it in case of something going wrong. This isn't enabled by
            # default.
            logging.info(f"[{message.guild.name}: {message.author} ({message.author.id})] : {message.content}")

        database.execute_command('UPDATE counter SET all_messages = all_messages + 1')
        await bot.process_commands(message)

    bot.add_cog(Listener(bot))
