from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    
@bot.command()
async def yattaze(ctx):
    await ctx.send('やったぜ')
        
        
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

    
@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

    
@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

    
@bot.cmmands()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")        
        
        
token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
