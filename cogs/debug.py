import logging

from discord.ext import commands


class Debug(commands.Cog):
    """Debug Commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True, brief='Loads an extension.')
    @commands.check(commands.is_owner())
    async def load(self, ctx, extension_name: str):
        """
        Loads an extension.
        """
        with ctx.message.channel.typing():
            try:
                self.bot.load_extension(extension_name)
            except (AttributeError, ImportError) as e:
                await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
                return
            logging.info("{} loaded.".format(extension_name))
            await ctx.send("{} loaded.".format(extension_name))

    @commands.command(hidden=True, brief='Unloads an extension.')
    @commands.check(commands.is_owner())
    async def unload(self, ctx, extension_name: str):
        """
        Unloads an extension.
        """
        with ctx.message.channel.typing():
            self.bot.unload_extension(extension_name)
        logging.info("{} unloaded.".format(extension_name))
        await ctx.send("{} unloaded.".format(extension_name))

    @commands.command(hidden=True, brief='Reloads an extension.')
    @commands.check(commands.is_owner())
    async def reload(self, ctx, extension_name: str):
        """
        Reloads an extension.
        """
        with ctx.message.channel.typing():
            try:
                self.bot.unload_extension(extension_name)
                logging.info("{} unloaded.".format(extension_name))
                self.bot.load_extension(extension_name)
                logging.info("{} loaded.".format(extension_name))
            except (AttributeError, ImportError) as e:
                await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
                return
        await ctx.send("{} reloaded.".format(extension_name))


def setup(bot):
    bot.add_cog(Debug(bot))
