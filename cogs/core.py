import sys
import time

import discord
from discord.ext import commands

from cogs.internal import database


class Core(commands.Cog):
    """Core features of the Bot."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Pings the Bot and the Discord Servers.')
    async def ping(self, ctx):
        """
        Pings the Bot and the Discord Servers
        Acknowledge (ACK) =  Time the bot needs to know that its a command.
        Hearbeat = Time the bot needs to ping the Server / to send the message
        """
        # Time the time required to send a message first.
        # This is the time taken for the message to be sent, awaited, and then
        # for discord to send an ACK TCP header back to you to say it has been
        # received; this is dependant on your bot's load (the event loop latency)
        # and generally how shit your computer is, as well as how badly discord
        # is behaving.
        start = time.monotonic()
        msg = await ctx.send('Pinging...')
        millis = (time.monotonic() - start) * 1000
        # Since sharded bots will have more than one latency, this will average them if needed.
        heartbeat = ctx.bot.latency * 1000
        await msg.edit(content=f':heart: **{heartbeat:,.2f} ms**\t:file_cabinet: **{millis:,.2f} ms**.')

    @commands.command(brief="Sets the Language of your server!", usage=["german, english"])
    @commands.has_permissions(administrator=True)
    async def language(self, ctx, message):
        database.execute_command(f'UPDATE server SET language = "{message}" WHERE serverId = {ctx.guild.id};')
        await ctx.send("Server language successfully Changed!")

    @commands.command(hidden=True, brief='Executes a Command in the Database')
    @commands.check(commands.is_owner())
    async def execute(self, ctx, *, message):
        """
        Executes a command in the Database.
        Should only be used by the Owner to setup the Database.
        """
        msg = await ctx.send('Executing the Command..')
        result = database.execute_command(message)
        await msg.edit(content="Executed Command! Response:\n" + result)

    @commands.command(hidden=True, aliases=["shutdown"], brief='Shutdown or restarts the Bot.')
    @commands.check(commands.is_owner())
    async def restart(self, ctx):
        """
        Shutdown or restarts the Bot.
        It leaves the chat and changes the status. It should only be run by the Owner.
        """
        try:
            await ctx.cleanup(ctx.guild)
        except:
            print("")
        await ctx.send("Shutting down / Restarting... :wave:")
        time.sleep(3)
        await self.bot.change_presence(
            activity=discord.Activity(name='with the Restart Button!', type=discord.ActivityType.playing),
            status=discord.Status.dnd)
        self.bot.logout()
        await sys.exit()


def setup(bot):
    bot.add_cog(Core(bot))
