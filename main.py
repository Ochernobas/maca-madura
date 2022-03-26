import discord
import sorteio
from discord.ext import commands

cogs = [sorteio]
client = commands.Bot(command_prefix="=")

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("Token")
