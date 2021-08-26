import discord
import os
from discord.ext import commands,tasks
import asyncio
import random
import math
import datetime
import time

#########################
###########||############
#######\\##||##//########
########\\####//#########
#####____#######____#####
########//####\\#########
#######//##||##\\########
###########||############
#########################

client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
    global ConsoleChannel
    ConsoleChannel = client.get_channel(856882963107282967)
    await ConsoleChannel.send("{0.user} ready to serve mother Anarchy.".format(client))
    global DMChannel
    DMChannel = client.get_channel(872522936165228574)

@client.event
async def on_message(message):
  global mention
  mention = f'<@!{client.user.id}>'
  if message.author == client.user:
    return
  if mention in message.content and not message.content.startswith("?"):
        await message.reply("มีปัญหาหรอไอ้เหี้ย")
  if message.content.startswith(message.content) and message.author.id != 854008226697314384 and message.author.id != 875405857414864896:
      if message.channel.type == discord.ChannelType.private:
            DM = str(message.author.name+str(message.author.id)+" wrote DM "+  "'"+message.content+"'")
            await DMChannel.send(DM)

  await client.process_commands(message)

@client.command()
async def send(ctx,channelID : int,txt):
  SendChannel = client.get_channel(channelID)
  await SendChannel.send(txt)

@client.command()
async def DM(ctx,user : discord.User,txt):
  await user.send(txt)

@client.event
async def on_command_error(ctx,error):
    await ctx.send(error)

@client.command()
async def time(ctx):
    local_time = datetime.datetime.now()
    current = datetime.datetime.now().strftime("%H:%M:%S")
    await ctx.send("Year:"+str(local_time.year)+"\n Month-date:"+str(local_time.month)+":"+str(local_time.day)+"\n Time:"+str(current))

@client.command()
async def print(ctx,*,txt):
    await ctx.send(txt)

@client.command()
async def quote(ctx,txt,ID : discord.Member=None):
    if ID == None:
        await ctx.send('"'+txt+'"' '\n' '\n       -{0}, {1}'.format(ctx.author,datetime.datetime.now().year))
    else:
        await ctx.send('"'+txt+'"' '\n' '\n       -{0}, {1}'.format(ID,datetime.datetime.now().year))

@client.command()
async def ask(ctx,*,question):
    fixedYesAns = ["Is Francesc bad?"]
    fixedNoAns = ["Is Francesc good?"]
    if "?" in question:
        if question in fixedYesAns:
            await ctx.reply("Yes!")
        elif question in fixedNoAns:
            await ctx.reply("No!")
        else:
            ans = ["Yes!","No!","Not sure","Probably","Probably not"]
            await ctx.reply(random.choice(ans))
    else:
        await ctx.reply("question must have \"?\"")

@client.command()
async def shutdown(ctx):
  if ctx.author.id == 557878180518821903:
    await ctx.send("Good bye")
    await asyncio.sleep(2)
    quit()

def main(TOKEN):
    client.run(TOKEN)