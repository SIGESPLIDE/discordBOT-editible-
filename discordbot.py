# -*- coding: utf-8 -*-
# 必要なパッケージを読み込み
import discord
import os
import datetime
import random
import time

# ボットの定義
client = discord.Client()
prefix = "$"

#起動時にコール
@client.event
async def on_ready():
    print("%sでログインしました" % (client.user.name))
    count = len(client.guilds)
    activityData = discord.Activity(
        name="$help | "+str(len(client.guilds))+"鯖で放流中",
        type=discord.ActivityType.playing
    )
    await client.change_presence(activity=activityData)

# チャットに反応
@client.event
async def on_message(message):
    # ログ表示
    date = datetime.datetime.now()
    print("[%s] <%s> %s" % (date.strftime('%Y年%m月%d日 %H:%M:%S'), message.author,message.content))

    # botチェック
    if message.author.bot:
        return

    # ｺﾏﾝﾄﾞ応答
    if isPrefix(message,"ping"):
        await message.channel.send("pong")
        return
    if isPrefix(message,"yattaze"):
        await message.channel.send("やったぜ")
        return
    if isPrefix(message,"greet"):
        await message.channel.send(":smiley: :wave: Hello, there!")
        return
    if isPrefix(message,"cat"):
        await message.channel.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
        return
    if isPrefix(message,"omikuji"):
        OmikujiList = ['大吉', '吉', '中吉', '小吉', '半吉', '末吉', '末小吉', '平', '凶', '小凶', '半凶', '末凶', '大凶']
        await message.channel.send("あなたの運勢は" + random.choice(OmikujiList) + "です")
        return
    if isPrefix(message,"info"):
        embedData = discord.Embed(title="SIGESBOT", description="", color=discord.Colour(0x112f43), timestamp=datetime.datetime.now())
        embedData.add_field(name="Author", value="@SIGES_SSSPlide#6921", inline=False)
        embedData.add_field(name="Joined Servers", value=f"{len(client.guilds)}", inline=False)
        embedData.add_field(name="Invite", value="https://discord.com/api/oauth2/authorize?client_id=933370022296965160&permissions=8&scope=bot", inline=False)
        embedData.set_author(name="SIGES_SSSPlide", url="https://github.com/SIGESPLIDE/discordBOT-editible-", icon_url="https://cdn.discordapp.com/avatars/360028497202118657/32420042fa4b4550bdc66a747089da14.webp?size=128")
        embedData.set_thumbnail(url="https://cdn.discordapp.com/avatars/933370022296965160/8255741edc4afc8f9735197825b92185.webp?size=100")
        embedData.set_footer(text="this is Pre-release Discord bot")
        await message.channel.send(embed=embedData)
        return
    if message.content.startswith(prefix):
        await message.add_reaction("❓")


def isPrefix(message,word):
    if message.content == prefix+word:
        return True
    return False


#async def add(ctx, a: int, b: int):
#    await ctx.send(a + b)


#@bot.command()
#async def multiply(ctx, a: int, b: int):
#    await ctx.send(a * b)


#@bot.command()
#async def division(ctx, a: int, b: int):
#    if a == 0:
#        await ctx.send("Are you serious?!")
#    elif b == 0:
#        await ctx.send("No way")
#    else:
#        await ctx.send(a / b)

client.run(os.getenv('BOT_TOKEN'))
