import discord
from discord.ext import commands
from discord import app_commands
from parsegbx import parsegbx
import datetime
import re
import time
import sys

backslash = "/"
currentDateAndTime = time.localtime()
currentTime = time.strftime("%H:%M", currentDateAndTime)
logName = f"{datetime.date.today()}:{currentTime}"
logFileName = logName.replace(":", "-")
newline = "\n"
intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents = intents, help_command=None)
sys.stdout = open(f"./Trackmaniabot/logs/{logFileName}.log", "w")

def sep_num_chars(s):
    res = re.split('([-+]?\d+\.\d+)|([-+]?\d+)', s.strip())
    res_f = [r.strip() for r in res if r is not None and r.strip() != '']
    return res_f


@client.event
async def on_ready():
    print("Bot is running")
    await client.change_presence(status=discord.Status.online)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="uhhhhhhuhhh"))
    try:
        sync = await client.tree.sync()
        print("Synced")
    except:
        print(sys.exc_info)

#@client.event
#async def on_message(message):
#    print("messag recieved")
#    if message.channel.id == 662035765252980794:
#        if str(message.attachments) == "[]":
#            print("no attachments")
#            return
#        else:
#            print(message.attachments)
#            split_v1 = str(message.attachments).split("filename='")[1]
#            filename = str(split_v1).split("' ")[0]
#            print(filename)
#            if filename.endswith(".gbx"): 
#                await message.attachments[0].save(fp="ReplayStorage/{}".format(filename))
#                parsedGBXFile = parsegbx(filename)

@client.command()
async def update(ctx):
    finished = False
    counter = 0
    print("Update called")
    toEdit = await ctx.message.channel.send("Processing")
    try:
        while finished == False:
            while counter < 3:
                await toEdit.edit(content=f"Processing"+(counter+1)*".")
                counter += 1
                time.sleep(0.5)
                if counter > 2: 
                    counter = -1
    except Exception as e:
        print(f"Error occured while sending processing message. Details: {e}")
    strinb = ctx.message.content
    
            






client.run("MTA2Nzc5OTM0OTMxNDIxMTkxMQ.GUpz6D.p7_LpgUFCkT1Q43Volz9YYkAQTJGCuZkZHJHqM")
