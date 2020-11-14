from discord.ext import commands


class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Sends a Text in the name of the Bot.", usage=["hello world!"])
    async def say(self, ctx, *, message):
        """
        Sends a Text message in the name of the Bot.
        BEWARE: Messages get Logged in case of Abusal!
        """
        await ctx.message.delete()
        await ctx.send(message)


def setup(bot):
    bot.add_cog(Say(bot))
