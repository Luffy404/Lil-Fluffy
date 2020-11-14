import discord
from discord.ext import commands

from cogs.internal import requests


class Fun(commands.Cog):
    """Entertaining Command."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Call someone an idiot!', usage='@Mad Luffy#3039')
    async def baka(self, ctx, member: discord.Member = None):
        """
        Call someone an idiot
        """
        data = await requests.get_data('https://nekos.life/api/v2/img/baka')
        image_url = data["url"]
        embed = discord.Embed().set_image(url=image_url) \
            .set_footer(icon_url=ctx.message.author.avatar_url, text=f"Requested by {ctx.message.author.name}")
        embed.title = 'BAKA!'
        if member is not None:
            embed.description = f'{member.mention}'
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))
