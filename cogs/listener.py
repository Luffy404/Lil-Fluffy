import json
from pathlib import Path
from textwrap import dedent
import logging
from discord.ext import commands
from discord.ext.commands import Bot


with open(str(Path().parent.absolute()) + "\\config.json") as fp:
    config = json.load(fp)
    QUESTIONMARK = config["QUESTIONMARK"]
    LOG_MESSAGES = config["LOG_MESSAGES"]
    fp.close()


class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Prints out some info about the bot once it's started and ready to use"""
        bot_app_info = (await Bot.application_info(self.bot))

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
            await bot.process_commands(message)

    bot.add_cog(Listener(bot))
