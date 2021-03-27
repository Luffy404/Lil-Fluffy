from discord.ext import commands
from libneko import pag
from mcstatus import MinecraftServer

from cogs.internal import database


class Minecraft(commands.Cog):
    """Events for the Bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Sets the IP of your minecraft server!", usage=["127.0.0.1:25565"], aliases=["setserver"])
    @commands.has_permissions(administrator=True)
    async def setServer(self, ctx, message):
        serverIp, serverPort = message.split(':')
        database.execute_command(
            f'UPDATE server SET serverIp = "{serverIp}", serverPort = "{serverPort}" WHERE serverId = {ctx.guild.id};')
        await ctx.send("Server successfully Changed!")

    @commands.command(brief="Shows the current status of the Minecraft server!", aliases=["mcstatus", "mc"])
    async def minecraft(self, ctx):
        serverIp = database.execute_command_fetchall(f'SELECT serverIp FROM server WHERE serverId = {ctx.guild.id};')
        serverPort = database.execute_command_fetchall(
            f'SELECT serverPort FROM server WHERE serverId = {ctx.guild.id};')
        server = MinecraftServer.lookup(f'{serverIp[0][0]}:{serverPort[0][0]}')
        status = server.status()
        query = server.query()
        navigator = pag.EmbedNavigatorFactory()
        navigator += f"There are {status.players.online} out of {status.players.max} players on the server online!\n" \
                     f"The Server has a {status.latency}ms ping!\n\n" \
                     f"Players:\n" \
                     f"{', '.join(query.players.names)}"
        navigator.start(ctx)


def setup(bot):
    bot.add_cog(Minecraft(bot))
