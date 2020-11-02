from discord.ext import commands
import logging


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Information(bot))
