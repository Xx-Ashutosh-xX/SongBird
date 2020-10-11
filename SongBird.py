'''
Developer : Ashutosh Saxena
Date: 3/10/2020
Description : A simple Discord bot to play songs and send memes to a channel
'''

import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import shutil 
import time
from os import system
import aiohttp
import random

TOKEN = 'YOUR_BOT_TOKEN_HERE' # Bot Tokken
BOT_PREFIX = '-' # Bot prefix

bot = commands.Bot(command_prefix = BOT_PREFIX)
bot.remove_command('help') 


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print("Reloaded : " + str(extension))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')



@bot.event
async def on_ready():
    '''
    Prints Logged in when the Bot is Ready
    '''
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('-help for Cookies'))
    print('Logged in as : ' + bot.user.name + '\n')


bot.run(TOKEN)