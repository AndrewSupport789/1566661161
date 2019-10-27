import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
from discord.utils import get
import os

bot = commands.Bot(command_prefix='*')


TOKEN = 'NjM3MzE3NDc4NjIzNjA4ODQy.XbVnjQ.MMfJLNoJ-QmxX3R9AoGc9yyhQ4Y'

#BlackRabbit001

@bot.event
async def on_ready():
    print('Logged in as')
    print('------')
	
	
	
@bot.command()
@commands.has_role('Admin')
async def kick(ctx):
    await ctx.send(":smiley: :wave: Hello, there! :heart: ")

    


    
    
    
bot.run(os.getenv('BOT_TOKEN'))
