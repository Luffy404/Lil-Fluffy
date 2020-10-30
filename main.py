import discord

with open('token.secret')as file:
    TOKEN = file.read().strip()

client = discord.client()


client.run(TOKEN)

