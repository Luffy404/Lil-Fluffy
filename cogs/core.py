import time
from discord.ext import commands
import logging

from cogs import database


class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
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

    @commands.command(hidden=True)
    @commands.check(commands.is_owner())
    async def execute(self, ctx, *, message):
        msg = await ctx.send('Executing the Command..')
        result = database.execute_command(message)
        await msg.edit(content="Executed Command! Response:\n" + result.fetchall())


def setup(bot):
    bot.add_cog(Core(bot))
