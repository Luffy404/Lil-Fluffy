import random

import discord
from discord.ext import commands
from libneko import pag

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

    @commands.command(brief='Kiss someone when they last expect it!', usage='@Mad Luffy#3039')
    async def kiss(self, ctx, member: discord.Member = None):
        """
        Do a cute moment for cute people
        """
        data = await requests.get_data('https://nekos.life/api/v2/img/kiss')
        image_url = data["url"]
        embed = discord.Embed().set_image(url=image_url) \
            .set_footer(icon_url=ctx.message.author.avatar_url, text=f"Requested by {ctx.message.author.name}")
        embed.title = f'AWW HOW CUTE!'
        if member is not None:
            embed.description = f'{ctx.message.author.mention} has kissed {member.mention}!'
            await ctx.send(embed=embed)
        else:
            await ctx.send("Select a user!")

    @commands.command(brief='Feed someone!', usage='@Mad Luffy#3039')
    async def feed(self, ctx, member: discord.Member = None):
        """
        Feed someone something :heart:
        """
        data = await requests.get_data('https://nekos.life/api/v2/img/feed')
        image_url = data["url"]
        embed = discord.Embed().set_image(url=image_url) \
            .set_footer(icon_url=ctx.message.author.avatar_url, text=f"Requested by {ctx.message.author.name}")
        embed.title = f'Nom Nom Nom!'

        if member is not None:
            embed.description = f'{ctx.message.author.mention} has fed {member.mention}!'
            await ctx.send(embed=embed)
        else:
            await ctx.send("Select a user!")

    @commands.command(brief='genetically engineered Catgirls at its finest!')
    async def gecg(self, ctx):
        """
        Shows what you should'nt invest to.
        """
        data = await requests.get_data('https://nekos.life/api/v2/img/gecg')
        image_url = data["url"]
        embed = discord.Embed().set_image(url=image_url) \
            .set_footer(icon_url=ctx.message.author.avatar_url, text=f"Requested by {ctx.message.author.name}")

        embed.title = 'True Story'
        await ctx.send(embed=embed)

    @commands.command(brief='Smug at someone or something!', usage='@Mad Luffy#3039')
    async def smug(self, ctx, *, message=None):
        """
        smug about something
        """
        data = await requests.get_data('https://nekos.life/api/v2/img/smug')
        image_url = data["url"]
        embed = discord.Embed().set_image(url=image_url) \
            .set_footer(icon_url=ctx.message.author.avatar_url, text=f"Requested by {ctx.message.author.name}")

        if message is not None:
            embed.title = f"{ctx.message.author.name} is smugging about {message}!"
        else:
            embed.title = f"{ctx.message.author.name} is smugging."
        await ctx.send(embed=embed)

    @commands.command(brief='poke someone!', usage='@Mad Luffy#3039')
    async def poke(self, ctx, member: discord.Member = None):
        """
        Poke someone!
        """
        data = await requests.get_data('https://nekos.life/api/v2/img/poke')
        image_url = data["url"]
        embed = discord.Embed().set_image(url=image_url) \
            .set_footer(icon_url=ctx.message.author.avatar_url, text=f"Requested by {ctx.message.author.name}")
        embed.title = f'Hey, Wake Up!'

        if member is not None:
            embed.description = f'{ctx.message.author.mention} has poked {member.mention}!'
            await ctx.send(embed=embed)
        else:
            await ctx.send("Select a user!")

    @commands.command(brief='Shame on you!', usage='@Mad Luffy#3039')
    async def slap(self, ctx, member: discord.Member = None):
        """
        Slap someone when they did something wrong
        """
        data = await requests.get_data('https://nekos.life/api/v2/img/slap')
        image_url = data["url"]
        embed = discord.Embed().set_image(url=image_url) \
            .set_footer(icon_url=ctx.message.author.avatar_url, text=f"Requested by {ctx.message.author.name}")
        embed.title = f'Shame on you!'

        if member is not None:
            embed.description = f'{ctx.message.author.mention} has slapped {member.mention}!'
            await ctx.send(embed=embed)
        else:
            await ctx.send("Select a user!")

    @commands.command(brief='Pat someone!', usage='@Mad Luffy#3039')
    async def pat(self, ctx, member: discord.Member = None):
        """
        Pat someone :heart:
        """
        data = await requests.get_data('https://nekos.life/api/v2/img/pat')
        image_url = data["url"]
        embed = discord.Embed().set_image(url=image_url) \
            .set_footer(icon_url=ctx.message.author.avatar_url, text=f"Requested by {ctx.message.author.name}")
        embed.title = f'Awww!'

        if member is not None:
            embed.description = f'{ctx.message.author.mention} has patted {member.mention}!'
            await ctx.send(embed=embed)
        elif member is ctx.message.author:
            embed.description = f'{ctx.message.author.mention} has patted himself!'
            await ctx.send(embed=embed)
        else:
            await ctx.send("Select a user!")

    @commands.command(brief='hug someone!', usage='@Mad Luffy#3039')
    async def hug(self, ctx, member: discord.Member = None):
        """
        Hugs someone :heart:
        """

        data = await requests.get_data('https://nekos.life/api/v2/img/hug')
        image_url = data["url"]
        embed = discord.Embed().set_image(url=image_url) \
            .set_footer(icon_url=ctx.message.author.avatar_url, text=f"Requested by {ctx.message.author.name}")
        embed.title = f'Awww!'

        if member is not None:
            embed.description = f'{ctx.message.author.mention} has hugged {member.mention}!'
            await ctx.send(embed=embed)
        else:
            await ctx.send("Select a user!")

    @commands.command(brief='Shows a random neko picture!')
    async def catgirl(self, ctx):
        """
        Lets you see a random Neko picture
        """
        data = await requests.get_data('https://nekos.life/api/v2/img/hug')
        image_url = data["url"]
        embed = discord.Embed().set_image(url=image_url) \
            .set_footer(icon_url=ctx.message.author.avatar_url, text=f"Requested by {ctx.message.author.name}")
        embed.title = f'Meow!'
        await ctx.send(embed=embed)

    @commands.command(brief='Flip a Coin!')
    async def flip(self, ctx):
        """
        Flips a coin, what did you expect? Possible outcome: "Head", "Tails"
        """
        outputcmd = ['Head!', 'Tails!']
        await ctx.send(random.choice(outputcmd))

    @commands.command(brief='Decides about your life!', aliases=['8ball', '8'], usage='Should I go outside today?')
    async def ball(self, ctx):
        """
        When you can't decide, so you need to ask a bot..
        """
        data = await requests.get_data('https://nekos.life/api/v2/img/8ball')
        image_url = data["url"]
        embed = discord.Embed().set_image(url=image_url) \
            .set_footer(icon_url=ctx.message.author.avatar_url, text=f"Requested by {ctx.message.author.name}")
        response = data["url"]
        embed.set_image(url=response)
        await ctx.send(embed=embed)

    @commands.command(brief='Throws you a random fact at your head!')
    async def fact(self, ctx):
        """
        Gives you a random fact!
        """
        data = await requests.get_data('https://nekos.life/api/v2/fact')
        embed = discord.Embed().set_footer(icon_url=ctx.message.author.avatar_url,
                                           text=f"Requested by {ctx.message.author.name}")
        embed.title = data["fact"]

        await ctx.send(embed=embed)

    @commands.command(brief='Shower thoughts for everyone!')
    async def shower(self, ctx):
        """
        When someone asks to many questions im gonna respond with questions they cant awnser instantly!
        """
        data = await requests.get_data('https://nekos.life/api/v2/why')
        embed = discord.Embed().set_footer(icon_url=ctx.message.author.avatar_url,
                                           text=f"Requested by {ctx.message.author.name}")
        embed.title = data["why"]

        await ctx.send(embed=embed)

    @commands.command(brief='Get an inspirational quote!')
    async def quote(self, ctx):
        """
        Get an inspirational quote! (API based, i didnt create the quotes)
        """
        data = await requests.get_data('https://opinionated-quotes-api.gigalixirapp.com/v1/quotes')

        product1 = data["quotes"]
        product2 = product1[0]
        quote = product2["quote"]
        author = product2["author"]
        await ctx.send(f"`{quote}`\n by `{author}`")

    @commands.command(brief='Get a random poem!')
    async def poem(self, ctx):
        """
        Get a random poem! (API based, i didnt create the poems)
        """
        message = await ctx.send("Please wait till I get the data from the Server!")
        data = await requests.get_data('https://www.poemist.com/api/v1/randompoems')

        firstpoem = data[0]
        firsttitle = firstpoem["title"]
        firstcontent = firstpoem["content"]
        await message.delete()
        nav = pag.EmbedNavigatorFactory(max_lines=20)
        nav += f"{firsttitle} \n\n {firstcontent}"
        nav.start(ctx)

    @commands.command(brief='Random geek Memes!')
    async def xkcd(self, ctx):
        """
        xkcd is a online meme page wich contains geek jokes.
        """
        data = await requests.get_data('http://xkcd.com/info.0.json')
        maxnum = data["num"]
        randomNo = random.randint(1, maxnum)
        data = await requests.get_data(f'http://xkcd.com/{randomNo}/info.0.json')

        imageURL = data["img"]
        embed = discord.Embed().set_image(url=imageURL) \
            .set_footer(icon_url=ctx.message.author.avatar_url, text=f"Requested by {ctx.message.author.name}")
        embed.title = f"XKCD Meme No. {randomNo}"
        await ctx.send(embed=embed)

    @commands.command(brief='Shows all emojis from the guilds im in.', usage='thonk', aliases=['emoji'])
    async def emojis(self, ctx, message=None):
        """
        Shows all emojis from the guilds im in. You can add a name behind the command to search for emojis.
        """
        if message is not None:
            e = ''
            nav = pag.EmbedNavigatorFactory()
            for i2 in self.bot.guilds:
                for i in list(i2.emojis):
                    if message in i.name:
                        e += f'{discord.utils.get(self.bot.emojis, name=i.name)} '
            try:
                await ctx.send(e)
            except:
                nav += "I cant show all in one page, since Discord only allows 2000 Chars per message.\n"
                nav += e
        else:
            e = ''
            for i2 in self.bot.guilds:
                for i in list(i2.emojis):
                    e += f'{discord.utils.get(self.bot.emojis, name=i.name)} '
            nav = pag.EmbedNavigatorFactory()

            nav += "I cant show all in one page, since Discord only allows 2000 Chars per message.\n"
            nav += e
            nav.start(ctx)


def setup(bot):
    bot.add_cog(Fun(bot))
