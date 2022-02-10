from discord.ext import commands
from os import getenv
import traceback
import discord
import datetime
import random


bot = commands.Bot(command_prefix='$')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@client.event
async def on_ready():

# 認識しているサーバーをlist型で取得し、その要素の数を 変数:guild_count に格納
    guild_count = len(client.guilds)
# 関数:lenは、引数に指定したオブジェクトの長さや要素の数を取得
    game = discord.Game(f'{guild_count} 鯖で稼働中')
# BOTのステータスを変更する
    await client.change_presence(status=discord.Status.online, activity=game)
# パラメーターの status でステータス状況(オンライン, 退席中など)を変更可能




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
    embed.set_footer(text="this is Pre-release Discord bot")
    await ctx.send(embed=embed)


@bot.command()
async def omikuji(ctx):
    OmikujiList = ['大吉', '吉', '中吉', '小吉', '半吉', '末吉', '末小吉', '平', '凶', '小凶', '半凶', '末凶', '大凶']
    await ctx.send("あなたの運勢は" + random.choice(OmikujiList) + "です")


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
