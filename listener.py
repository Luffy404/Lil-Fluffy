from textwrap import dedent
import logging
from discord.ext import commands
from discord.ext.commands import Bot


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


def setup(bot):
    bot.add_cog(Listener(bot))
