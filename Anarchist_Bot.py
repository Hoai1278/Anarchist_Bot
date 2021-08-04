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

TOKEN1 = "ODcyNTE1MDQ3ODQxMjI2NzUy.YQq-9Q.G8ILwUBHW9g7e5ZyC4UwaMzfVRI"
client.run(TOKEN1)