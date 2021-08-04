import discord
import os
from discord.ext import commands,tasks
import asyncio
import random
import math
import datetime
import time

client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
    global ConsoleChannel
    ConsoleChannel = client.get_channel(856882963107282967)
    await ConsoleChannel.send("{0.user} ready to serve mother Anarchy.".format(client))

TOKEN1 = "HyLkBKa6LeFzW9Bsau7xI6LepxCKnaGg"
client.run(TOKEN1)