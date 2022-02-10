import discord
from discord.ext import commands
from os import getenv
import traceback
import datetime
import random


client = discord.Client()
guild_count = len(client.guilds)
bot = commands.Bot(command_prefix='$')


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
    await ctx.send(a + b)


@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a * b)


@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")


@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="SIGESBOT", description="", color=discord.Colour(0x112f43), timestamp=datetime.datetime.now())
    embed.add_field(name="Author", value="@SIGES_SSSPlide#6921", inline=False)
    embed.add_field(name="Joined Servers", value=f"{len(bot.guilds)}", inline=False)
    embed.add_field(name="Invite", value="https://discord.com/api/oauth2/authorize?client_id=933370022296965160&permissions=8&scope=bot", inline=False)
    embed.set_author(name="SIGES_SSSPlide", url="https://github.com/SIGESPLIDE/discordBOT-editible-", icon_url="https://cdn.discordapp.com/avatars/360028497202118657/32420042fa4b4550bdc66a747089da14.webp?size=128")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/933370022296965160/8255741edc4afc8f9735197825b92185.webp?size=100")
    embed.set_footer(text="this is Pre-release Discord bot")
    await ctx.send(embed=embed)


@bot.command()
async def omikuji(ctx):
    OmikujiList = ['大吉', '吉', '中吉', '小吉', '半吉', '末吉', '末小吉', '平', '凶', '小凶', '半凶', '末凶', '大凶']
    await ctx.send("あなたの運勢は" + random.choice(OmikujiList) + "です")


bot=commands.Bot(activity=discord.Game(f'{guild_count} 鯖で稼働中'))


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
