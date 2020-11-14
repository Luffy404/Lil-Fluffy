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

    @commands.command(brief='Shows a neko gif!')
    async def ngif(self, ctx):
        """
        Shows an Gif about a Neko
        """
        data = await requests.get_data('https://nekos.life/api/v2/img/ngif')
        image_url = data["url"]
        embed = discord.Embed().set_image(url=image_url) \
            .set_footer(icon_url=ctx.message.author.avatar_url, text=f"Requested by {ctx.message.author.name}")
        embed.title = 'Meow!'
        await ctx.send(embed=embed)

    @commands.command(brief='CATS EVERYWHERE', aliases=['cat'])
    async def meow(self, ctx):
        """
        Shows a cute cat pic!
        """
        data = await requests.get_data('https://nekos.life/api/v2/img/meow')
        image_url = data["url"]
        embed = discord.Embed().set_image(url=image_url) \
            .set_footer(icon_url=ctx.message.author.avatar_url, text=f"Requested by {ctx.message.author.name}")
        embed.title = 'Meow!'
        await ctx.send(embed=embed)

    @commands.command(brief='Tickle a User!', usage='@Mad Luffy#3039')
    async def tickle(self, ctx, member: discord.Member = None):
        """
        Tickle someone like it said before.
        """
        data = await requests.get_data('https://nekos.life/api/v2/img/meow')
        image_url = data["url"]
        embed = discord.Embed().set_image(url=image_url) \
            .set_footer(icon_url=ctx.message.author.avatar_url, text=f"Requested by {ctx.message.author.name}")
        embed.title = f'Tickle!'
        if member is not None:
            embed.description = f'{ctx.message.author.mention} has tickled {member.mention}!'
            await ctx.send(embed=embed)
        else:
            await ctx.send("Select a user!")


def setup(bot):
    bot.add_cog(Fun(bot))
