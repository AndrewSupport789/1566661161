import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
from discord.utils import get
import os
from discord.utils import get
from discord import Game
from discord import Activity, ActivityType

bot = commands.Bot(command_prefix='Supp')


MSG = '   Enjoy'

REMIN = 'Just click on "continue" button there'

#BlackRabbit001



@bot.event
async def on_ready():
    await bot.wait_until_ready()
    await bot.change_presence(activity=Activity(name="Supporters channel", type=ActivityType.watching))


	
@bot.command()
@commands.has_role('Supporter')
async def Nord(ctx):
    await ctx.author.send("***NordVPN***")
    await ctx.author.send("*LINK #1:* https://link-to.net/52237/566455615Nord" + MSG)
    await ctx.author.send("*LINK #2:* https://link-to.net/52237/Nord551607600" + MSG)
    await ctx.author.send("*LINK #3:* https://link-to.net/52237/Nord5789902" + MSG)
    await ctx.send("Check your DMs :heart:" + MSG)
 
@Nord.error
async def test_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('''Buy supporter role here: http://Shoppy.gg/@BadRabbit001''')
 
@bot.command()
@commands.has_role('Supporter')
async def Spotify(ctx):
    await ctx.author.send("***Spotify***")
    await ctx.author.send("*LINK #1:* https://link-to.net/52237/578421500Spotify" + MSG)
    await ctx.author.send("*LINK #2:* https://link-to.net/52237/Spotify024579" + MSG)
    await ctx.send("Check your DMs :heart:" + MSG)
    
@Spotify.error
async def test_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('''Buy supporter role here: http://Shoppy.gg/@BadRabbit001''')
    
@bot.command()
@commands.has_role('Supporter')
async def Minecraft(ctx):
    await ctx.author.send("***Minecraft***")
    await ctx.author.send("*LINK #1:* https://link-to.net/52237/Minecraft555469" + MSG)
    await ctx.author.send("*LINK #2:* https://link-to.net/52237/Minecraft2456789" + MSG)
    await ctx.author.send("*LINK #3:* https://link-to.net/52237/Minecraft8794201" + MSG)
    await ctx.send("Check your DMs :heart:" + MSG)

@Minecraft.error
async def test_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('''Buy supporter role here: http://Shoppy.gg/@BadRabbit001''')    
    

@bot.command()
@commands.has_role('Supporter')
async def Steam(ctx):
    await ctx.author.send("***Steam***")
    await ctx.author.send("*LINK #1:* https://link-to.net/52237/Steam00018973" + MSG)
    await ctx.author.send("*LINK #2:* https://link-to.net/52237/21576Steam" + MSG)
    await ctx.send("Check your DMs :heart:" + MSG)

@Steam.error
async def test_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('''Buy supporter role here: http://Shoppy.gg/@BadRabbit001''')
#
 
@bot.command()
@commands.has_role('Supporter')
async def Uplay(ctx):
    await ctx.author.send("***Uplay***")
    await ctx.author.send("*LINK #1:* https://link-to.net/52237/WDH0Uplay0225fgk" + MSG)
    await ctx.author.send("*LINK #2:* https://link-to.net/52237/0225516Uplay0089" + MSG)
    await ctx.author.send("*LINK #2:* https://link-to.net/52237/2225Uplay2240" + MSG)
    await ctx.send("Check your DMs :heart:" + MSG)	
	
@Uplay.error
async def test_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('''Buy supporter role here: http://Shoppy.gg/@BadRabbit001''')	
	
@bot.command()
@commands.has_role('Supporter')
async def Origin(ctx):
    await ctx.author.send("***Origin***")
    await ctx.author.send("*LINK #1:* https://link-to.net/52237/Origin55555781" + MSG)
    await ctx.author.send("*LINK #2:* https://link-to.net/52237/Origin202503 " + MSG)
    await ctx.send("Check your DMs :heart:" + MSG)
 
@Origin.error
async def test_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('''Buy supporter role here: http://Shoppy.gg/@BadRabbit001''')
 #
@bot.command()
@commands.has_role('Supporter')
async def Hulu(ctx):
    await ctx.author.send("***Hulu***")
    await ctx.author.send("*LINK #1:* https://link-to.net/52237/Hulu549797" + MSG)
    await ctx.author.send("*LINK #2:* https://link-to.net/52237/21576Hulu" + MSG)
    await ctx.author.send("*LINK #3:* https://link-to.net/52237/Hulu00124693" + MSG)
    await ctx.send("Check your DMs :heart:" + MSG)

@Hulu.error
async def test_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('''Buy supporter role here: http://Shoppy.gg/@BadRabbit001''')
        
@bot.command()
@commands.has_role('Supporter')
async def Grammarly(ctx):
    await ctx.author.send("***Grammarly***")
    await ctx.author.send("*LINK #1:* https://link-to.net/52237/Grammarly00128973" + MSG)
    await ctx.send("Check your DMs :heart:" + MSG)
 
@Grammarly.error
async def test_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('''Buy supporter role here: http://Shoppy.gg/@BadRabbit001''')
 
@bot.command()
@commands.has_role('Supporter')
async def Crunchyroll(ctx):
    await ctx.author.send("***Crunchyroll***")
    await ctx.author.send("*LINK #1:* https://link-to.net/52237/Crunchyroll564879" + MSG)
    await ctx.author.send("*LINK #2:* https://link-to.net/52237/Crunchyroll5648789" + MSG)
    await ctx.send("Check your DMs :heart:" + MSG)

@Crunchyroll.error
async def test_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('''Buy supporter role here: http://Shoppy.gg/@BadRabbit001''')
	
	
bot.run(os.getenv('BOT_TOKEN'))
