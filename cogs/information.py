import json
import platform
import time

import discord
import psutil
from discord.ext import commands
from discord.ext.commands import Bot

import main
from cogs import database

bot_uptime = main.bot_uptime


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['info', 'information'], brief='Shows Information about the Bot.')
    async def status(self, ctx):
        """
        Shows some Information about the Bot.
        """
        with open('config.json') as fp:
            config = json.load(fp)
            extensions = config["COGS"]
            prefixes = config["PREFIXES"]

        all_messages = database.execute_command_fetchall('SELECT all_messages from counter')
        all_commands = database.execute_command_fetchall('SELECT all_commands from counter')
        completed_commands = database.execute_command_fetchall('SELECT completed_commands from counter')
        lines_of_code = database.execute_command_fetchall('SELECT loc from counter')
        highest_loc = database.execute_command_fetchall('SELECT highest_loc from counter')
        chars_in_total = database.execute_command_fetchall('SELECT chars_in_total from counter')
        highest_chars_in_total = database.execute_command_fetchall('SELECT highest_chars_in_total from counter')
        allcogs = ''
        allguilds = 0
        allchannel = 0
        allusers = 0
        cogs = 0
        total_commands = 0
        total_ram_mb = psutil.virtual_memory().total / 1024 / 1024
        used_ram_mb = psutil.virtual_memory().used / 1024 / 1024
        free_ram_mb = psutil.virtual_memory().free / 1024 / 1024
        ram_usage_percentage = psutil.virtual_memory().percent
        cpu_usage_percentage = psutil.cpu_percent()
        avg_commands_per_message = "%.2f" % (all_commands[0][0] / all_messages[0][0])
        application_info = await Bot.application_info(self.bot)
        total_uptime = time.monotonic() - bot_uptime
        mins, secs = divmod(total_uptime, 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        weeks, days = divmod(days, 7)
        uptime = f"**{int(weeks)}** Weeks\n" \
                 f"**{int(days)}** Days\n" \
                 f"**{int(hours)}** Hours\n" \
                 f"**{int(mins)}** Minutes\n" \
                 f"**{int(secs)}** Seconds"

        for extension in extensions:
            cogs += 1
            allcogs += f"{extension}.py\n"
        for guild in self.bot.guilds:
            allguilds += 1
            for _ in guild.channels:
                allchannel += 1
            for _ in guild.members:
                allusers += 1
        for _ in self.bot.commands:
            total_commands += 1

        avg_messages_per_user = "%.2f" % (all_messages[0][0] / allusers)
        avg_user_per_guild = "%.2f" % (allusers / allguilds)
        avg_channel_per_guild = "%.2f" % (allchannel / allguilds)

        embed = discord.Embed(title="by Mad Luffy", color=0xF9006F)
        embed.set_author(name="Lil' Luffy", url='https://discord.gg/XZazRvchjP',
                         icon_url=application_info.icon_url)
        embed.set_thumbnail(url=application_info.icon_url)
        embed.add_field(name="Uptime ", value=uptime, inline=True)
        embed.add_field(name="Prefixes ", value=prefixes, inline=True)
        embed.add_field(name="Stats",
                        value=f"**{platform.system()} {platform.release()}**\n"
                              f"RAM:\n**{total_ram_mb: .2f}MiB**\n"
                              f"Used Ram:\n**{used_ram_mb: .2f}MiB**\n"
                              f"Free Ram:\n**{free_ram_mb: .2f}MiB**\n"
                              f"Ram Usage: **{ram_usage_percentage}%**\n"
                              f"CPU Usage: **{cpu_usage_percentage}%**",
                        inline=True)
        embed.add_field(name="Lines of Code & Chars in Total ",
                        value=f"LoC:\n**{lines_of_code[0][0]}**\n"
                              f"Highest LoC:\n**{highest_loc[0][0]}**\n"
                              f"Characters in Total:\n**{chars_in_total[0][0]}**\n"
                              f"Highest Characters in Total:\n**{highest_chars_in_total[0][0]}**",
                        inline=True)
        embed.add_field(name=f"Extensions (**{cogs}**) ",
                        value=f"All Commands: **{total_commands}**\n"
                              f"**{allcogs}**", inline=True)
        embed.add_field(name="Various Information",
                        value=f"Guilds: **{allguilds}**\n"
                              f"Channels: **{allchannel}**\n"
                              f"Users: **{allusers}**\n"
                              f"Failed Commands: **{all_commands[0][0] - completed_commands[0][0]}**\n"
                              f"Commands Used:\n**{all_commands[0][0]}**\n"
                              f"All Messages:\n**{all_messages[0][0]}**",
                        inline=True)
        embed.add_field(name="Average Information",
                        value=f"Avg. Messages per User:\n**{avg_messages_per_user}**\n"
                              f"Avg. Users per Guild:\n**{avg_user_per_guild}**\n"
                              f"Avg. Channel per Guild:\n**{avg_channel_per_guild}**\n"
                              f"Avg. Commands per Message:\n**{avg_commands_per_message}**",
                        inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
