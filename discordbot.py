# -*- coding: utf-8 -*-
# ----------必要なパッケージを読み込み----------
# 標準パッケージじゃない
from ast import Index
from webbrowser import get
import timeout_decorator
import discord
import youtube_dl
#from requests import get
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get

# 標準パッケージ
import datetime
import random
import re
import os
import asyncio


#　YOUTUBE_DL用定義
# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


# ----------ボットの定義----------
client = discord.Client()
prefix = "\$"
list_OKNO  = ['👍','👎']
list_yesno = ['⭕', '❌']
list_vote = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']

# text系関数
def isCommand(message,match):
    return re.match("^"+prefix+match,message.content)

@timeout_decorator.timeout(1)
def mathEval(message):
    try:
        ans = eval(re.sub(prefix+"eval ","",message.content))
        return ans
    except Exception as e:
        return ("```cs\n# Error : %s ```" % str(e))

# 起動時にコール
@client.event
async def on_ready():
    print("%sでログインしました" % (client.user.name))
    count = len(client.guilds)
    activityData = discord.Activity(
        name="$help | "+str(len(client.guilds))+"鯖で放流中 | |\n\b\f利用規約、Readmeをよく読んでから導入，利用しましょう|\\ver.0.16.1",
        type=discord.ActivityType.playing
    )
    await client.change_presence(activity=activityData)

# ----------チャットに反応----------
@client.event
async def on_message(message):
    # ログ表示
    JST        = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
    date       = datetime.datetime.now(JST)
    print(f"[{date.strftime('%Y年%m月%d日 %H:%M:%S')}] {message.guild.name} >> {message.channel.name} >> {message.author.name}:{message.content}")
    # botチェック
    if message.author.bot:
        return

    # ----------ｺﾏﾝﾄﾞ応答----------
    if isCommand(message,"num(|ber)$"):
        for i in range(len(list_vote)):
            await message.add_reaction(list_vote[i])
        return
    # オウム返し
    if isCommand(message,"rep(|eat)$") or isCommand(message,"rep(|eat)"):
        await message.delete()
        try:
            repData  = message.content.split("\\")
            repType  = repData[1]
        except Exception as e:
            print(e.args)
        try:
            await message.channel.send(repType)
        except IndexError:
            await message.channel.send("文字が入力されていません。'''$repeat'''の後ろに文字を入れてください")
        except Exception as e:
            print(e.args)
        return
    # オウム返し２
    if isCommand(message,"oumu$"):
        await message.channel.send("このコマンドはターミナルから入力をする時に使うコマンドです")
        oumu = input("ここに文字を入力してオウム返し-->")
        await message.channel.send(oumu)
        return
    # お遊び要素
    if isCommand(message,"あなたは(|ロボットですか？)$"):
        await message.add_reaction("❌")
        async with message.channel.typing():
            await asyncio.sleep(5)
        msg = await message.reply("ﾆﾝｹﾞﾝﾀﾞﾖ")
        await msg.add_reaction("⭕")

        return
    if isCommand(message,"ffmpeg$"):
        kami = "<:kami:933925948259205171>"
        try:
            await message.add_reaction(kami)
            msg = await message.channel.send(kami)
            await msg.add_reaction(kami)
        except Exception as e:
            print(e.args)
        return
    if isCommand(message,"(shibanyan|shibanyaan|しばねこ|しばにゃん|シバニャン|芝猫|芝ねこ|芝ネコ|さぎねこ|さぎにゃん詐欺にゃん|詐欺ねこ|詐欺猫|サギねこ|サギ猫)"):
        sore = "<:sore:933926434907521064>"
        kusa = "<:kusa:933925678867423263>"
        try:
            await message.channel.send(sore+"は"+kusa)
        except Exception as e:
            print(e.arg)
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
    if isCommand(message,"add [0-9]+?"):
        data = re.findall(r'\d+',message.content)
        ans = 0
        for i in range(len(data)):
            ans += int(data[i])
        await message.reply(ans)
        return
    # 引き算
    if isCommand(message,"add [0-9]+?"):
        data = re.findall(r'\d+',message.content)
        ans = 0
        for i in range(len(data)):
            ans += int(data[i])
        await message.reply(ans)
    # 掛け算
    if isCommand(message,"mul [0-9]+?"):
        data = re.findall(r'\d+',message.content)
        ans = 0
        for i in range(len(data)):
            ans *= int(data[i])
        await message.reply(ans)
        return
    # 割り算
    if isCommand(message,"div [0-9]+?"):
        data = re.findall(r'\d+',message.content)
        ans = float(data[0])
        try:
            for i in range(len(data)-1):
                ans /= int(data[i+1])
            await message.reply(ans)
        except ZeroDivisionError:
            await message.reply("are you serious?!")
        return
    # eval関数を利用した四則演算
    if isCommand(message,"eval .*"):
        await message.reply(mathEval(message))
        return
    # SIGES BOTのインフォメーションをembed形式で表示
    if isCommand(message,"info$"):
        embedData = discord.Embed(
            title       = "SIGESBOT",
            description = "",
            color       = discord.Colour(0x112f43),
            timestamp   = date)
        embedData.add_field(
            name   = "Author",
            value  = "@SIGES_SSSPlide#6921",
            inline = False)
        embedData.add_field(
            name   = "Joined Servers",
            value  = f"{len(client.guilds)}",
            inline = False)
        embedData.add_field(
            name   = "Invite",
            value  = "https://discord.com/api/oauth2/authorize?client_id=933370022296965160&permissions=140727766081&scope=bot",
            inline = False)
        embedData.set_author(
            name     = "SIGES_SSSPlide",
            url      = "https://github.com/SIGESPLIDE/discordBOT-editible-",
            icon_url = "https://cdn.discordapp.com/avatars/360028497202118657/32420042fa4b4550bdc66a747089da14.webp?size=128")
        embedData.set_thumbnail(
            url = "https://cdn.discordapp.com/avatars/933370022296965160/8255741edc4afc8f9735197825b92185.webp?size=100")
        embedData.set_footer(
            text = "this is Pre-release Discord bot")
        await message.channel.send(embed=embedData)
        return
    #----------ここからpoll機能----------
    if isCommand(message,"que(|stion) (yes(|-no)|ok(|-no)|vote|help)"):
        # セパレータによる不自然な挙動を防止
        if re.match(".*\s{2,}",message.content):
            await message.channel.send("無効なコマンドです (セパレータが連続もしくは最後に入力されています)")
            return

        # 項目作成
        pollData  = message.content.split(" ")
        pollType  = pollData[1]
        if not (pollType == "help"):
            pollTitle = pollData[2]
            pollData  = pollData[3:]
        # 分岐
        try:
            # OK-NO 疑問文
            if pollType == "ok-no" or pollType == "ok":
                # 質問文を表示
                embed = discord.Embed(title=pollTitle, description="", color=discord.Colour.blue())
                voting_msg = await message.channel.send(embed=embed)
                # リアクション追加
                for i in range(len(list_OKNO)):
                    await voting_msg.add_reaction(list_OKNO[i])
                return
            # Yes-No 疑問文
            if pollType == "yes-no" or pollType == "yes":
                # 質問文を表示
                embed = discord.Embed(title=pollTitle, description="", color=discord.Colour.blue())
                voting_msg = await message.channel.send(embed=embed)
                # リアクション追加
                for i in range(len(list_yesno)):
                    await voting_msg.add_reaction(list_yesno[i])
                return
            # 選択肢のある疑問文　
            if pollType == "vote":
                # 選択肢の数を確認
                select = len(pollData)
                if select > 10:
                    await message.channel.send("可能な選択肢は最大10個までです")
                    return
                # 質問文を表示
                embed = discord.Embed(title=pollTitle, description="", color=discord.Colour.green())
                for i in range(len(pollData)):
                    embed.description = embed.description + list_vote[i] + "   " + pollData[i] + "\n"
                voting_msg = await message.channel.send(embed=embed)
                # リアクション追加
                for i in range(select):
                    await voting_msg.add_reaction(list_vote[i])
                return
            # ヘルプの表示
            if pollType == "help":
                #文の表示
                embed = discord.Embed(title="使用方法", description="", color=discord.Colour.red())
                embed.description = (
                    '**question [TYPE] [CONTENT] [CANDIDATE]**\n'
                    '注意 : 質問文や選択肢に"空欄"を含めないでください\n'
                    '\n'
                    '**[TYPE] : "yes-no" or "vote"**\n'
                    '__"yes-no" :__\n'
                    'Yes-No疑問文を作成します\n'
                    '[CANDIDATE]は必要ありません\n'
                    '__"vote" :__\n'
                    '選択肢が複数ある質問を作成します\n'
                    '[CANDIDATE]がない場合は質問文だけ表示されます\n'
                    '\n'
                    '**[CONTENT] :**\n'
                    '質問文に相当します\n'
                    '\n'
                    '**[CANDIDATE] :**\n"'
                    '質問形式が\"vote\"である場合の選択肢です\n'
                    '選択肢として可能な最大個数は10個までです')
                await message.channel.send(embed=embed)
                return

            # 以上のどの形式でもないものは形式不備を伝える
            else:
                await message.channel.send("質問形式が異なっています (2つめの引数が正しくありません)")
                return

        except IndexError:
            await message.channel.send("質問の入力形式に間違いがあります (引数が足りません)")
            return
    # 使用可能コマンドを確認
    if isCommand(message,"help$"):
        embedData = discord.Embed(title = "使用可能コマンド一覧", description = "現在メンテナンス中", color = discord.Colour(0x2ecc71))
        embedData.add_field(name = "**__$number__**", value = "１から１０までの数字のリアクションを追加します")
        embedData.set_thumbnail(url = "https://cdn.discordapp.com/emojis/933926187619733545.webp?size=96&quality=lossless")
        '''
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**__$number__**", value = "ping値を返します", inline = False)
        '''
        await message.channel.send(embed=embedData)
        return
    # なんだっけ
    #if hoegehoge == hage:
    #---------------実装予定のvoice機能-----------------#
    '''
    # Suppress noise about console usage from errors
    if isCommand(message, "join$"):
        if message.author.voice is None:
            await message.channel.send("接続先が見つかりません")
            return
        # ボイスチャンネルに接続する
        await message.channel.send("joined!")
        await message.author.voice.channel.connect()
        return

    if isCommand(message, "leave$"):
        if message.guild.voice_client is None:
            await message.channel.send("leaving")
            return

        # 切断する
        await message.guild.voice_client.disconnect()
        return

    if isCommand(message, "play https://youtu\.be/"):
        # video, source = search(query)
        #voice = get(bot.voice_clients, guild=message.guild)
        #await message.send(f"Now playing {info['title']}.")

        #voice.play(FFmpegPCMAudio(source, **FFMPEG_OPTS), after=lambda e: print('done', e))
        #voice.is_playing()

        # youtubeから音楽をダウンロードする
        # player = await YTDLSource.from_url(url, loop=client.loop)

        # await message.guild.voice_client.play(player)

        # await message.channel.send('playing{}'.format(player.title))
        return

    if isCommand(message, "stop$"):
        if message.guild.voice_client is None:
            return

        # 再生中ではない場合は実行しない
        if not message.guild.voice_client.is_playing():
            await message.channel.send("再生中ではありません")
            return

        message.guild.voice_client.stop()

        await message.channel.send("stopped!")
        return
        '''
    if isCommand(message,".*$"):
        await message.add_reaction("❓")
        await message.add_reaction("🤔")


# Bot起動
client.run(os.getenv('BOT_TOKEN'))
