# -*- coding: utf-8 -*-
# 必要なパッケージを読み込み
from sqlite3 import Timestamp
import discord
import os
import datetime
import random
import re
import asyncio

# ボットの定義
client = discord.Client()
prefix = "\$"

# 起動時にコール
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
    JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
    date = datetime.datetime.now(JST)
    print("[%s] <%s> %s" % (date.strftime('%Y年%m月%d日 %H:%M:%S'), message.author,message.content))

    # botチェック
    if message.author.bot:
        return

    # ｺﾏﾝﾄﾞ応答
    if isCommand(message,"number$"):
        await message.add_reaction("0️⃣")
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await message.add_reaction("3️⃣")
        await message.add_reaction("4️⃣")
        await message.add_reaction("5️⃣")
        await message.add_reaction("6️⃣")
        await message.add_reaction("7️⃣")
        await message.add_reaction("8️⃣")
        await message.add_reaction("9️⃣")
        return
    if isCommand(message,"あなたはロボットですか？$"):
        await message.add_reaction("❌")
        await message.reply("ﾆﾝｹﾞﾝﾀﾞﾖ")
        return
    if isCommand(message,"ping$"):
        raw_ping = client.latency
        ping = round(raw_ping * 1000)
        await message.reply(f"Pong!\nSIGES BotのPing値は{ping}msです。")
        return
    if isCommand(message,"yattaze$"):
        await message.reply("やったぜ")
        return
    if isCommand(message,"greet$"):
        await message.reply(":smiley: :wave: Hello, there!")
        return
    if isCommand(message,"cat$"):
        await message.reply("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
        return
    if isCommand(message,"omikuji$"):
        OmikujiList = ['大吉', '吉', '中吉', '小吉', '半吉', '末吉', '末小吉', '平', '凶', '小凶', '半凶', '末凶', '大凶']
        await message.reply("あなたの運勢は" + random.choice(OmikujiList) + "です")
        return
    if isCommand(message,"add [0-9]+ [0-9]+$"):
        data = re.findall(r'\d+',message.content)
        await message.reply(int(data[0])+int(data[1]))
        return
    if isCommand(message,"mul [0-9]+ [0-9]+$"):
        data = re.findall(r'\d+',message.content)
        await message.reply(int(data[0])*int(data[1]))
        return
    if isCommand(message,"div [0-9]+ [0-9]+$"):
        data = re.findall(r'\d+',message.content)
        await message.reply(int(data[0])/int(data[1]))
        return
    if isCommand(message,"eval .*"):
        try:
        #    await message.reply(eval(re.sub(prefix+"eval ","",message.content)))
            await asyncio.wait_for(await message.reply(eval(re.sub(prefix+"eval ","",message.content))), timeout=1)
        except Exception as e:
            await message.reply(":thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face:\n```cs\n# Error : %s ```:thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face:" % str(e.args))
        return
    if isCommand(message,"info$"):
        embedData = discord.Embed(title="SIGESBOT", description="", color=discord.Colour(0x112f43), timestamp = date)
        embedData.add_field(name="Author", value="@SIGES_SSSPlide#6921", inline=False)
        embedData.add_field(name="Joined Servers", value=f"{len(client.guilds)}", inline=False)
        embedData.add_field(name="Invite", value="https://discord.com/api/oauth2/authorize?client_id=933370022296965160&permissions=8&scope=bot", inline=False)
        embedData.set_author(name="SIGES_SSSPlide", url="https://github.com/SIGESPLIDE/discordBOT-editible-", icon_url="https://cdn.discordapp.com/avatars/360028497202118657/32420042fa4b4550bdc66a747089da14.webp?size=128")
        embedData.set_thumbnail(url="https://cdn.discordapp.com/avatars/933370022296965160/8255741edc4afc8f9735197825b92185.webp?size=100")
        embedData.set_footer(text="this is Pre-release Discord bot")
        await message.channel.send(embed=embedData)
        return
    if isCommand(message,"help$"):
        embedData = discord.Embed(title = "使用可能コマンド一覧", description = "現在メンテナンス中", color = discord.Colour(0x2ecc71))
        embedData.add_field(name = "**__$number__**", value = "０から９までの数字のリアクションを追加します")
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        await message.channel.send(embed=embedData)
        return
    if isCommand(message,".*$"):
        await message.add_reaction("❓")
        await message.add_reaction("🤔")


def isCommand(message,match):
    return re.match("^"+prefix+match,message.content)


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
