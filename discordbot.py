# -*- coding: utf-8 -*-
# ----------必要なパッケージを読み込み----------
from sqlite3 import Timestamp
import discord
import os
import datetime
import random
import re
import asyncio
import time

# ----------ボットの定義----------
client = discord.Client()
prefix = "\$"

#poll機能用の定義

list_yesno = ['⭕', '❌']
list_vote = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']

def emphasize(text):
    return "**" + text + "**"

def underline(text):
    return "__" + text + "__"

def isContainedNoInput(command):
    for i in command:
        if i == "":
            return True
    return False

# 起動時にコール
@client.event
async def on_ready():
    print("%sでログインしました" % (client.user.name))
    count = len(client.guilds)
    activityData = discord.Activity(
        name="$help | "+str(len(client.guilds))+"鯖で放流中 | |\n\b利用規約、Readmeをよく読んでから導入，利用しましょう|\\ver.0.15",
        type=discord.ActivityType.playing
    )
    await client.change_presence(activity=activityData)

# ----------チャットに反応----------
@client.event
async def on_message(message):
    # ログ表示
    JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
    date = datetime.datetime.now(JST)
    print("[%s] <%s> %s" % (date.strftime('%Y年%m月%d日 %H:%M:%S'), message.author,message.content))

    # botチェック
    if message.author.bot:
        return

    # ----------ｺﾏﾝﾄﾞ応答----------
    if isCommand(message,"number$") or isCommand(message,"num$"):
        for i in range(len(list_vote)):
            await message.add_reaction(list_vote[i])
        return
    # お遊び要素
    if isCommand(message,"あなたはロボットですか？$"):
        await message.add_reaction("❌")
        await message.reply("ﾆﾝｹﾞﾝﾀﾞﾖ")
        time.sleep(10)
        await message.add_reaction("❌")
        return
    # SIGES BOTのping値を返します
    if isCommand(message,"ping$"):
        raw_ping = client.latency
        ping = round(raw_ping * 1000)
        await message.reply(f"Pong!\nSIGES BotのPing値は{ping}msです。")
        return
    # 「やったぜ」と返す
    if isCommand(message,"yattaze$"):
        await message.reply("やったぜ")
        return
    # BOTが返信して挨拶する
    if isCommand(message,"greet$"):
        await message.reply(":smiley: :wave: Hello, there!")
        return
    # ”giphy”からgif画像を取って貼り付ける（ねこ）
    if isCommand(message,"cat$"):
        await message.reply("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
        return
    # おみくじを引く
    if isCommand(message,"omikuji$"):
        OmikujiList = ['大吉', '吉', '中吉', '小吉', '半吉', '末吉', '末小吉', '平', '凶', '小凶', '半凶', '末凶', '大凶']
        await message.reply("あなたの運勢は" + random.choice(OmikujiList) + "です")
        return
    # 足し算
    if isCommand(message,"add [0-9]+ [0-9]+$"):
        data = re.findall(r'\d+',message.content)
        await message.reply(int(data[0])+int(data[1]))
        return
    # 掛け算
    if isCommand(message,"mul [0-9]+ [0-9]+$"):
        data = re.findall(r'\d+',message.content)
        await message.reply(int(data[0])*int(data[1]))
        return
    # 割り算
    if isCommand(message,"div [0-9]+ [0-9]+$"):
        data = re.findall(r'\d+',message.content)
        try:
            print(int(data[0])/int(data[1]))
            await message.reply(int(data[0])/int(data[1]))
        except ZeroDivisionError:
            await message.reply("are you serious?!")
        return
    # eval関数を利用した四則演算
    if isCommand(message,"eval .*"):
        try:
        #    await message.reply(eval(re.sub(prefix+"eval ","",message.content)))
            await asyncio.wait_for(await message.reply(eval(re.sub(prefix+"eval ","",message.content))), timeout=1)
        except Exception as e:
            await message.reply(":thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face:\n```cs\n# Error : %s ```:thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face::thinking_face:" % str(e.args))
        return
    # SIGES BOTのインフォメーションをembed形式で表示
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
    
    #----------ここからpoll機能----------
    pollcommand = message.content.split(" ")
    # 投票関連のコマンド
    if pollcommand[0] == "$question":

        # セパレータによる不自然な挙動を防止
        if isContainedNoInput(pollcommand):
            await message.channel.send("無効なコマンドです (セパレータが連続もしくは最後に入力されています)")
            return

        try:
            # Yes-No 疑問文
            if pollcommand[1] == "yes-no":
                embed = discord.Embed(title=pollcommand[2], description="", color=discord.Colour.blue())

                # 質問文を表示してYes,Noを絵文字でリアクション
                voting_msg = await message.channel.send(embed=embed)
                for i in range(len(list_yesno)):
                    await voting_msg.add_reaction(list_yesno[i])
                return

            # 選択肢のある疑問文　
            elif pollcommand[1] == "vote":
                embed = discord.Embed(title=pollcommand[2], description="", color=discord.Colour.green())

                # 選択肢の数を確認
                select = len(pollcommand) - 3
                if select > 10:
                    await message.channel.send("可能な選択肢は最大10個までです")
                    return

                # 選択肢を表示
                vote_candidate = pollcommand[3:]
                for i in range(len(vote_candidate)):
                    embed.description = embed.description + list_vote[i] + "   " + vote_candidate[i] + "\n"

                # リアクションによる回答欄を作成
                voting_msg = await message.channel.send(embed=embed)
                for i in range(select):
                    await voting_msg.add_reaction(list_vote[i])
                return

            # 使い方
            elif pollcommand[1] == "help":
                embed = discord.Embed(title="使用方法", description="", color=discord.Colour.red())
                embed.description = emphasize("question [TYPE] [CONTENT] + [CANDIDATE]\n") + \
                                    "注意 : 質問文や選択肢に\"空欄\"を含めないでください\n" \
                                    "\n" \
                                    + emphasize("[TYPE] : \"yes-no\" or \"vote\"\n") + \
                                    underline("\"yes-no\" : \n") + \
                                    "Yes-No疑問文を作成します\n" \
                                    "[CANDIDATE]は必要ありません\n" \
                                    + underline("\"vote\" : \n") + \
                                    "選択肢が複数ある質問を作成します\n" \
                                    "[CANDIDATE]がない場合は質問文だけ表示されます\n" \
                                    "\n" \
                                    + emphasize("[CONTENT] : \n") + \
                                    "質問文に相当します\n" \
                                    "\n" \
                                    + emphasize("[CANDIDATE] : \n") + \
                                    "質問形式が\"vote\"である場合の選択肢です\n" \
                                    "選択肢として可能な最大個数は10個までです\n"
                await message.channel.send(embed=embed)
                return

            # 以上のどの形式でもないものは形式不備を伝える
            else:
                await message.channel.send("質問形式が異なっています (2つめの引数が正しくありません)")
                return
        
        except IndexError:
            await message.channel.send("質問の入力形式に間違いがあります (引数が足りません)")
            return
    '''# 使用可能コマンドを確認
    if isCommand(message,"help$"):
        embedData = discord.Embed(title = "使用可能コマンド一覧", description = "現在メンテナンス中", color = discord.Colour(0x2ecc71))
        embedData.add_field(name = "**__$number__**", value = "１から１０までの数字のリアクションを追加します")
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
    '''

    if isCommand(message,".*$"):
        await message.add_reaction("❓")
        await message.add_reaction("🤔")


def isCommand(message,match):
    return re.match("^"+prefix+match,message.content)



client.run(os.getenv('BOT_TOKEN'))
