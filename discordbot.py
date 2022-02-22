# -*- coding: utf-8 -*-

# -------------------------------------------- #
# --------　必要なパッケージを読み込み　-------- #
# -------------------------------------------- #

# 標準パッケージじゃない
from webbrowser import get
import timeout_decorator
import discord
#import youtube_dl
#from requests import get

# 標準パッケージ
import datetime
import random
import re
import os
import asyncio


#　YOUTUBE_DL用定義
'''メンテナンス中
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
    def init(self, source, *, data, volume=0.5):
        super().init(source, volume)

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
'''

# ---------------------------------- #
# -------- 雑学集用クラス定義 ------- #
# ---------------------------------- #
class Zatugaku:
    def __init__(self, score, title, description, fromorkinds, url, thumbnail, point):
        for key,value in locals().items():
            if not key == "self":
                self.__dict__[key] = value

Zatulist = [Zatugaku(
                    "ホワイトタイガーは正確にはベンガルトラの白変種で、野生では見ることができなくなってしまったほどの珍しさ。",
                    "[トラは狩りの成功率が10%！？]",
                    "->トラの狩りの成功率はわずか10%ほどと、とても低いらしい...\n"+
                    "しかも狩りのチャンスは一日1～2回くらいだとか",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    "",
                    "0"
                    ),
            Zatugaku(
                    "あの可愛いウサギがまさかの...",
                    "[ウサギは自分のうんこを肛門から直に食べる。]",
                    "->植物だけを食べる動物の胃腸にすむバクテリアは、\n"+
                    "植物を分解することで増え、うんこと一緒に出てくるという。\n"+
                    "ウサギは、これを再び食べることでタンパク質などの栄養をとっているそうだ。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    "",
                    "1"
                    ),
            Zatugaku(
                    "コアラの主食であるユーカリには、猛毒の青酸やタンニンなどが含まれている。",
                    "[コアラはユーカリにふくまれる猛毒のせいで一日中寝ている。]",
                    "->この毒入りの葉っぱが食べられる体になったことで\n"+
                    "生存競争に勝ち残ったコアラだが、栄養も少なく解毒にエネルギーを費やすため、\n"+
                    "省エネで一日中寝るしかなくなってしまったという。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    "",
                    "2"
                    ),
            Zatugaku(
                    "あまりにも風が強いと、「明日は明日の風がふくさ」と狩りを諦めてしまう。",
                    "[サーバルは耳がよすぎて狩りができないことがある。]",
                    "->土の中にいるネズミの動きさえ感じとれるほど敏感な耳を持つサーバル。\n"+
                    "しかしビュービューと風が強くふく日はこの武器が仇となり、\n"+
                    "なかなか獲物の居場所が突き止められないことも。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    "",
                    "3"
                    ),
            Zatugaku(
                    "これが、毛皮の美しさから「森の貴婦人」といわれる由縁だ。",
                    "[オカピの体はオイルでテカテカ。]",
                    "->高温多湿な熱帯雨林にすむため、濡れて体温を下げないよう\n"+
                    "水をはじく油分たっぷりのオイリーな体液を身に纏ったオカピ。\n"+
                    "体はいつもテカり、触るとベトベトするだけでなく茶色の体液がついてしまう。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    "",
                    "4"
                    ),
            Zatugaku(
                    "約2センチの大きさで生まれたカンガルーの赤ちゃんはすぐにお母さんの袋の中に隠れてしまうため、生まれた日がよく分からない。",
                    "[カンガルーの誕生日はてきとう。]",
                    "->半年ほどお母さんの袋の中で育ち、袋からひょっこり顔を出した日を\n"+
                    "「初顔認知日」としてカンガルーの誕生日としているのだ。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    "",
                    "5"
                    ),
            Zatugaku(
                    "逆に両親は色が抜けて白くなってしまうが、白いとモテないので、\n"+
                    "子育て後はカロテンという色素を含む藍藻を食べて羽の色を必死に戻すそうだ。",
                    "[フラミンゴの体が赤いのは食べ物のせい。]",
                    "->生まれたては真っ白で、両親から口移しでもらうフラミンゴミルクという\n"+
                    "赤い液体を飲んで、徐々に羽が色づくフラミンゴ。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    "",
                    "6"
                    ),
            Zatugaku(
                    "飲みこんだ草を口に吐き戻し、よくかんで再び飲みこむ「反すう」を行うアルパカ。",
                    "[アルパカは気に入らないとゲロをはく。]",
                    "->ところが気に入らないことがあると、このゲロを相手めがけて吐きかけるというから衝撃的だ。\n"+
                    "このゲロには胃液も混ざっているため、とてもくさいらしいぞ。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    "",
                    "7"
                    ),
            Zatugaku(
                    "サソリの毒が効きにくい体で刺されても死なないというから、見た目のかわいさとは裏腹の強さだ。",
                    "[ミーアキャットは毒のある危険な生き物が好き。]",
                    "->獲物の少ない砂漠では、サソリ、ムカデ、ヘビなど毒を持つ生き物も貴重なミーアキャットの食料。\n"+
                    "子どもは大人から弱ったサソリを与えられ狩りの特訓を受けるという。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    "",
                    "8"
                    ),
            Zatugaku(
                    "",
                    "[もともと「パンダ」とはレッサーパンダのことだった。]",
                    "->「パンダ」は「竹を食べるもの」という意味のネパールの言葉が由来している。\n"+
                    "後にジャイアントパンダが発見され、小さいという意味の「レッサー」が付けられた。\n"+
                    "つまり「パンダ」の呼び名を、後から見つかったジャイアントパンダに奪われてしまったというわけだ。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    "",
                    "9"
                    ),
            Zatugaku(
                    "極めて知能が高いことで知られるチンパンジーは、人間のように遊びながら笑うこともしばしば。",
                    "[チンパンジーは自分で自分をくすぐって笑う。]",
                    "->しかしそれだけでは飽き足らず、自分でわきの下や足の裏をくすぐったり、\n"+
                    "石などのでこぼこした場所に体をこすりつけたりして笑顔を見せることもあるらしいぞ。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    "",
                    "10"
                    ),
            Zatugaku(
                    "その名の通り、スローロリスは動きがのろいサルの仲間。甘い樹液や果実のほか昆虫も食べるのだが、\n"+
                    "すばしっこい虫をどうやって捕まえるのだろうか？",
                    "[スローロリスは動きがスローすぎて虫にも気づいてもらえない。]",
                    "->実は昆虫は動きの遅いものは風景と見分けがつかず、スローに近づかれると簡単に捕まえられてしまうのだ。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    "",
                    "11"
                    ),
            Zatugaku(
                    "オオコノハズクはフクロウの仲間。普段はふっくらと愛らしい姿だが、\n"+
                    "敵を発見するとみるみるギューッと体を細くして木の枝に化けてしまう。",
                    "[アフリカオオコノハズクは敵を見つけるとやせこける。]",
                    "->しかしかくれんぼに失敗すると、今度は体を精一杯大きくしてクジャクのポーズで威嚇！痩せたり太ったり、大忙しなのである。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    "",
                    "12"
                    ),
            Zatugaku(
                    "その姿は、はたから見るとビーチに横たわるグラビアアイドルにそっくり。",
                    "[アカカンガルーはアイドル気取りでひと休みする。]",
                    "->数種類いるカンガルーの中でも体が最大で筋肉モリモリのアカカンガルーだが、弱点は暑さ。\n"+
                    "砂漠の地面に穴を掘ってお尻を突っ込み、冷たい地面に体をつけて熱を逃がすのだ。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    "",
                    "13"
                    ),
            Zatugaku(
                    "オス同士では、青ければ青いほど偉いという謎ルールまであるという。",
                    "[サバンナモンキーの金玉はスカイブルー。]",
                    "->思わず二度見してしまうほど真っ青な金玉を持つサバンナモンキー。\n"+
                    "大人になるにつれ皮膚が鮮やかに色づくのは、もちろんメスの気を引くため。子どもをつくる準備が整った合図なのだ。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    "",
                    "14"
                    ),
            Zatugaku(
                    "直射日光に当たっている室外機はとても熱く、室外機の温度を下げるだけでも随分冷却効率が上がり、結果的に電気代が下がります。",
                    "[エアコン代を節電する裏ワザ]",
                    "->夏になるとエアコン・クーラーをつけっぱなしにする方が多いのですが、\n"+
                    "中々冷えなくて困ることがありますよね。そんな時は、室外機の温度を下げてみましょう。",
                    "生活",
                    "https://kurashi-no.jp/I0023637",
                    "",
                    "15"
                    ),
            Zatugaku(
                    "実は、シャンプーはポリエチレンの手袋をはめて使うことで節約出来ます。",
                    "[シャンプーを節約する裏ワザ]",
                    "->「シャンプーを節約したい！」と考えている方が少ないのは、シャンプーを節約出来ないと思っているからかもしれません。\n"+
                    "手の汚れや皮脂は洗剤を吸い取っており、手袋をつけるだけで、約3分の1程度で同じ泡立ちが期待出来ます。",
                    "生活",
                    "https://kurashi-no.jp/I0023637",
                    "",
                    "16"
                    ),
            Zatugaku(
                    "お風呂の床は垢がたまる場所であり、中々美しい状態になりませんよね。そんな時は、今話題のオキシ漬けを試してみましょう！",
                    "[風呂床を綺麗にする裏ワザ]",
                    "->コストコで今売れている商品「オキシクリーン」をお風呂の床に使用して放っておくだけで\n"+
                    "驚くほど綺麗になります。放っておくだけの掃除方法は嬉しいですよね！",
                    "生活",
                    "https://kurashi-no.jp/I0023637",
                    "",
                    "17"
                    ),
            Zatugaku(
                    "電子レンジは汚れが飛び散っていて、しかも乾燥していると中々綺麗になりまえんよね。",
                    "[電子レンジ掃除の裏ワザ]",
                    "->そんな時は、水を入れたコップをチンして、水蒸気を壁にあててから掃除してみましょう！\n"+
                    "汚れがとれやすくなり、掃除時間が大幅短縮されますよ。\n"+
                    "重曹を入れれば更に効果が上がりますが、その際は念入りに拭き取るようにしましょう。",
                    "生活",
                    "https://kurashi-no.jp/I0023637",
                    "",
                    "18"
                    ),
            Zatugaku(
                    "洗濯機を回すのは中々時間がかかりますよね。",
                    "[脱水スピードを上げる裏ワザ]",
                    "->大量の洗濯物だと効果が薄れてしまいますが、少量であれば乾いたバスタオルを脱水時に入れるだけで\n"+
                    "脱水スピードが大幅上昇します。たかだかタオル一枚なのですが、とても効果がありますので試してみましょう！",
                    "生活",
                    "https://kurashi-no.jp/I0023637",
                    "",
                    "19"
                    ),
            Zatugaku(
                    "多くの方は、服をそのまま洗濯機に入れていますよね。",
                    "[服の汚れをしっかり落とす豆知識]",
                    "->しかし、汗の汚れや皮脂の汚れは、服の裏側についていますので、服を裏返しにして洗濯するだけで\n"+
                    "汚れの落ち方が良くなります。脱ぐときに裏返しにしておくだけで効果がありますので、簡単なのが嬉しいですよね！",
                    "生活",
                    "https://kurashi-no.jp/I0023637",
                    "",
                    "20"
                    ),
            Zatugaku(
                    "寒い季節が近づいてくると食べたくなるのが焼いも。",
                    "[焼き芋を簡単に作る裏ワザ]",
                    "->実は炊飯器で作れてしまうのです。画像のようにサツマイモを入れ\n"+
                    "水を3㎝くらいの高さまで入れて、炊飯ボタンを押すだけ。これでしっとり系の焼いもが簡単に作れてしまいます。",
                    "生活",
                    "https://kurashi-no.jp/I0023637",
                    "https://www.instagram.com/p/BNq8U00BRX7/?utm_source=ig_embed&ig_rid=e707ac23-175a-424b-aab2-0b2121bff4af",
                    "21"
                    ),
            Zatugaku(
                    "料理に欠かせないのが包丁。しかし、料理をするにつれ切れ味が悪くなっていきますよね。\n"+
                    "そんな時に試したいのが、アルミホイルで刃を研ぐ方法です。",
                    "[包丁を簡単に研ぐ裏ワザ]",
                    "->アルミホイルはとても薄いので、刃を研げるなんて信じられないという方もいるかもしれませんが\n"+
                    "何枚かに重ねたアルミホイルで覆って、包丁をひくだけで研げるのです！",
                    "生活",
                    "https://kurashi-no.jp/I0023637",
                    "",
                    "22"
                    ),
            Zatugaku(
                    "タイツを履いていると、パンプスを履いた時に脱げやすくなりますよね。",
                    "[タイツでかかとが脱げてしまうのを防ぐ裏ワザ]",
                    "->そんな時に便利なのが、ヘアスプレーです。ヘアスプレーは粘着力がありますので\n"+
                    "すべってしまう箇所にかけておくだけで脱げにくくなります。靴側にかけるのが基本ですが、タイツにかけても効果がありますよ！",
                    "生活",
                    "https://kurashi-no.jp/I0023637",
                    "",
                    "23"
                    ),
            Zatugaku(
                    "服に穴が開いてしまった時、多くの方が自分で縫って直していますよね。",
                    "[針の穴に糸を通す裏ワザ]",
                    "->そんな時にイライラするのが、針の穴に糸を通す作業です。実はここでもヘアスプレーが活躍します。\n"+
                    "糸の先端にヘアスプレーをかけてねじるだけで、糸がしっかり固まり、針穴に通すのがとても楽になりますよ！",
                    "生活",
                    "https://kurashi-no.jp/I0023637",
                    "",
                    "24"
                    ),
            Zatugaku(
                    "特に賃貸住まいだと、部屋が狭くなりがちですよね。",
                    "[部屋を広く見せる裏ワザ①]",
                    "->そんな時に行いたいのが、「棚の真ん中を開ける」方法です。\n"+
                    "狭い部屋でも収納出来るようにと、多くの方が棚に物を押し込んでいますが、\n"+
                    "棚の真ん中だけでも開けておくと部屋が広く見える効果があります。是非試してみましょう！",
                    "生活",
                    "https://kurashi-no.jp/I0023637",
                    "",
                    "25"
                    ),
            Zatugaku(
                None,
                None,
                None,
                None,
                None,
                None,
                None
            )
            # template here ↓↓
            #Zatugaku(
            #        "score",
            #        "[title]",
            #        "->des",
            #        "動物",
            #        "url",
            #        "thumbnail",
            #        "n"
            #        )
]
# -------------------------------
# ----------ボットの定義----------
# -------------------------------

client = discord.Client()
prefix = "\$"
list_OKNO  = ['👍','👎']
list_yesno = ['⭕', '❌']
list_vote = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']

# ##########text系関数##########
def isCommand(message,match):
    return re.match("^"+prefix+match,message.content)

@timeout_decorator.timeout(1)
def mathEval(message):
    try:
        ans = eval(re.sub(prefix+"eval ","",message.content))
        return ans
    except Exception as e:
        return ("```cs\n# Error : %s ```" % str(e))

# ##########起動時にコール##########
@client.event
async def on_ready():
    print("%sでログインしました" % (client.user.name))
    count = len(client.guilds)
    activityData = discord.Activity(
        name="$help | "+str(len(client.guilds))+"鯖で放流中 | |\n\b\f利用規約、Readmeをよく読んでから導入，利用しましょう|\\ver.0.16.7",
        type=discord.ActivityType.playing
    )
    await client.change_presence(activity=activityData)

async def errorMessage(message,err):
    # 入力待機
    async with message.channel.typing():
        await asyncio.sleep(2)
    # データ準備
    embedData       = discord.Embed(
        title       = "エラーが発生しました。",
        description = "可能であれば詳細を開発者にお伝えください。\nまたは、githubでissueを立てることも可能です"
    )
    embedData.add_field(
        inline  = False,
        name    = "Error Data:",
        value   = "\n```cs\n " +
        "# Uncaught ReferenceError : contents is missing\n" +
        f"| Error code :\"{err}\" |\n" +
        "|こちらのエラ―コ―ド|を開発者へお伝えください。```"
    )
    # 送信
    await message.channel.send(embed = embedData)

# ---------------------------------
# ----------チャットに反応----------
# ---------------------------------

@client.event
async def on_message(message):
    # ログ表示
    JST        = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
    date       = datetime.datetime.now(JST)
    print(f"[{date.strftime('%Y年%m月%d日 %H:%M:%S')}] {message.guild.name} >> {message.channel.name} >> {message.author.name}:{message.content}")

    # ----------botチェック----------
    if message.author.bot:
        return

    # ----------------------------
    # ----------ｺﾏﾝﾄﾞ応答----------
    # ----------------------------
    if isCommand(message,"num(|ber)$"):
        for i in range(len(list_vote)):
            await message.add_reaction(list_vote[i])
        return

    # ----------オウム返し----------
    if isCommand(message,"rep(|eat)$") or isCommand(message,"rep(|eat)"):
        await message.delete()

        try:
            repData  = message.content.split("\\")
            repType  = repData[1]
        except IndexError:
            embedData = discord.Embed(
                title       = "⚠️Error内容⚠️",
                description = "",
                color       = discord.Colour(0xED4245)
            )
            embedData.add_field(
                name  = "```Index Error```",
                value = "$repeatの後ろに*空白を入れずに*、"+"`\`"+"<--バックスラッシュ-- を入れて\nその後ろに繰り返したい文字を入れてください"
            )
            embedData.set_thumbnail(url = "https://cdn.discordapp.com/emojis/570190733978632214.webp?size=96&quality=lossless")
            await message.channel.send(embed = embedData)

        try:
            await message.channel.send(repType)
        except Exception as e:
            print(e.args)
        return

    # ----------オウム返し２----------
    if isCommand(message,"oumu$"):
        await message.channel.send("このコマンドはターミナルから入力をする時に使うコマンドです")
        oumu = input("ここに文字を入力してオウム返し-->")
        await message.channel.send(oumu)
        return

    # -----------------------------
    # ----------お遊び要素----------
    # -----------------------------

    if isCommand(message,"あなたは(|ロボットですか？)$"):
        await message.add_reaction("❌")
        async with message.channel.typing():
            await asyncio.sleep(5)
        msg = await message.reply("ﾆﾝｹﾞﾝﾀﾞﾖ")
        await msg.add_reaction("⭕")
        return

    # ----------”giphy”からgif画像を取って貼り付ける（ねこ）----------
    if isCommand(message,"cat$"):
        await message.reply("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
        return

    # ----------ffmpegは神----------
    if isCommand(message,"ffmpeg$"):
        kami = "<:kami:933925948259205171>"
        try:
            await message.add_reaction(kami)
            msg = await message.channel.send(kami)
            await msg.add_reaction(kami)
        except Exception as e:
            print(e.args)
        return

    # ----------しばにゃん -> それは草----------
    if isCommand(message,"(shibanyan|shibanyaan|しばねこ|しばにゃん|シバニャン|芝猫|芝ねこ|芝ネコ|さぎねこ|さぎにゃん|詐欺にゃん|詐欺ねこ|詐欺猫|サギねこ|サギ猫|しばねこさま|芝ねこ様|芝猫様|しばねこ様|しば猫さま|しば猫様)"):
        sore = "<:sore:933926434907521064>"
        kusa = "<:kusa:933925678867423263>"
        try:
            await message.channel.send(sore+"は"+kusa)
        except Exception as e:
            print(e.arg)

    # -------------------------------
    # ----------実用コマンド----------
    # -------------------------------

    # ----------雑学集ランダム表示[ErrorCode:000x{point}]----------
    if isCommand(message,"zatu(|gaku)"):
        data = random.choice(Zatulist)
        if not data or not data.description:
            await errorMessage(message,"Unknown Data L532")
            return

        else:
            embedData       = discord.Embed(
                title       = data.title,
                description = f"そんなの知らなかった！ ～{data.fromorkinds}に関する雑学～",
                url         = data.url
            )
            embedData.add_field(
                name  = data.score,
                value = "\n"+data.description
            )
            embedData.set_footer(
                text = "カテゴリー:"+data.fromorkinds
            )
            await message.channel.send(embed = embedData)
            return

    # ----------SIGES BOTのping値を返します----------
    if isCommand(message,"ping$"):
        raw_ping = client.latency
        ping = round(raw_ping * 1000)
        await message.reply(f"Pong!\nSIGES BotのPing値は{ping}msです。")
        return

    # ----------「やったぜ」と返す----------
    if isCommand(message,"yattaze$"):
        await message.reply("やったぜ")
        return

    # ----------BOTが返信して挨拶する----------
    if isCommand(message,"greet$"):
        await message.reply(":smiley: :wave: Hello, there!")
        return

    # ----------おみくじを引く----------
    if isCommand(message,"omikuji$"):
        OmikujiList = ['大吉', '吉', '中吉', '小吉', '半吉', '末吉', '末小吉', '平', '凶', '小凶', '半凶', '末凶', '大凶']
        await message.reply("あなたの運勢は" + random.choice(OmikujiList) + "です")
        return


    # ----------足し算----------
    if isCommand(message,"add [0-9]+?"):
        data = re.findall(r'\d+',message.content)
        ans = 0
        for i in range(len(data)):
            ans += int(data[i])
        await message.reply(ans)
        return

    # ----------引き算----------
    if isCommand(message,"add [0-9]+?"):
        data = re.findall(r'\d+',message.content)
        ans = 0
        for i in range(len(data)):
            ans += int(data[i])
        await message.reply(ans)

    # ----------掛け算----------
    if isCommand(message,"mul [0-9]+?"):
        data = re.findall(r'\d+',message.content)
        ans = 0
        for i in range(len(data)):
            ans *= int(data[i])
        await message.reply(ans)
        return

    # ----------割り算----------
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

    # ----------eval関数を利用した四則演算----------
    if isCommand(message,"eval .*"):
        await message.reply(mathEval(message))
        return



    # SIGES BOTのインフォメーションをembed形式で表示
    if isCommand(message,"info$"):
        embedData       = discord.Embed(
            title       = "SIGESBOT",
            description = "",
            color       = discord.Colour(0x112f43),
            timestamp   = date
        )
        embedData.add_field(
            name     = "Author",
            value    = "@SIGES_SSSPlide#6921",
            inline   = False
        )
        embedData.add_field(
            name     = "Joined Servers",
            value    = f"{len(client.guilds)}",
            inline   = False
        )
        embedData.add_field(
            name     = "Invite",
            value    = "https://discord.com/api/oauth2/authorize?client_id=933370022296965160&permissions=140727766081&scope=bot",
            inline   = False
        )
        embedData.set_author(
            name     = "SIGES_SSSPlide",
            url      = "https://github.com/SIGESPLIDE/discordBOT-editible-",
            icon_url = "https://cdn.discordapp.com/avatars/360028497202118657/32420042fa4b4550bdc66a747089da14.webp?size=128"
        )
        embedData.set_thumbnail(
            url = "https://cdn.discordapp.com/avatars/933370022296965160/8255741edc4afc8f9735197825b92185.webp?size=100"
        )
        embedData.set_footer(
            text = "this is Pre-release Discord bot"
        )
        await message.channel.send(embed=embedData)
        return

    if isCommand(message, "(splityen|spy) [0-9]?"):
        spyData = message.content.split(" ")
        spyType = int(spyData[1])
        money   = spyType

        try:
            embedData       = discord.Embed(
                title       = "金種逆算シミュレーター⌨️💰",
                description = f"金額:{money}円"
            )

            maisuu     = money // 10000
            money      = money % 10000
            embedData.add_field(
                name   = "一万円札（10,000yen）",
                value  = f"{maisuu}枚",
                inline = False
            )

            maisuu     = money // 5000
            money      = money % 5000
            embedData.add_field(
                name   = '五千円札（5,000yen）',
                value  = f"{maisuu}枚",
                inline = False
            )

            maisuu     = money // 1000
            money      = money % 1000
            embedData.add_field(
                name   = "千円札（1,000yen）",
                value  = f"{maisuu}枚",
                inline = False
            )

            maisuu     = money // 500
            money      = money % 500
            embedData.add_field(
                name   = "五百円玉（500yen）",
                value  = f"{maisuu}枚",
                inline = False
            )

            maisuu      = money // 100
            money       = money % 100
            embedData.add_field(
                name   = "百円玉（100yen）",
                value  = f"{maisuu}枚",
                inline = False
            )

            maisuu     = money // 50
            money      = money % 50
            embedData.add_field(
                name   = "五十円玉（50yen）",
                value  = f"{maisuu}枚",
                inline = False
            )

            maisuu     = money // 10
            money      = money % 10
            embedData.add_field(
                name   = "十円（10yen）",
                value  = f"{maisuu}枚",
                inline = False
            )

            maisuu     = money // 5
            money      = money % 5
            embedData.add_field(
                name   = "五円玉（5yen）",
                value  = f"{maisuu}枚",
                inline = False
            )

            embedData.add_field(
                name  = "一円玉（1yen）",
                value = f"{money}枚",
                inline = False
            )

            await message.channel.send(embed = embedData)
        except ValueError:
            await message.channel.send("エラー。数字以外の文字を検知しました。初めからやり直してください")
        return

    if isCommand(message, "com(|bineyen)"):
        comData = message.content.split(" ")
        comData = comData[1:10]
        if comData[0] == "help":
            embedData = discord.Embed(
                title = "$com使用例"
            )
            embedData.add_field(
                name  = "␣には空白(スペース)を入れてください",
                value = "$com␣1円の枚数␣5円の枚数␣10円の枚数␣50円の枚数␣100円の枚数␣500円の枚数␣1000円の枚数␣2000円の枚数␣5000円の枚数␣10000円の枚数"
            )
            return await message.channel.send(embed=embedData)
        select = len(comData)
        if select == 0:
            await message.channel.send("!各枚数は10項目です。各10項目に数字を入力してください")
            return

        sum = 0
        ilist = [1, 5, 10, 50, 100, 500, 1000, 2000, 5000, 10000]
        for i in range(len(comData)):
            try:
                m = int(comData[i])
                sum += m*ilist[i]

            except ValueError as e:
                quit(f"エラーが発生したのでプログラムを終了します\nエラー＝{e.args}")

        await message.channel.send(f"合計金額は{sum}円です")
        print(f"合計金額は{sum}円です")
        return

    # ----------------------------------- #
    # --------　ここからpoll機能　-------- #
    # ----------------------------------- #
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
        try:# ----------------------------------OK-NO 疑問文------------------------------------- #
            if pollType == "ok-no" or pollType == "ok":
                # 質問文を表示
                embed = discord.Embed(title=pollTitle, description="", color=discord.Colour.blue())
                voting_msg = await message.channel.send(embed=embed)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
                # リアクション追加
                for i in range(len(list_OKNO)):
                    await voting_msg.add_reaction(list_OKNO[i])
                return

            # --------------------------------Yes-No 疑問文-------------------------------------- #
            if pollType == "yes-no" or pollType == "yes":
                # 質問文を表示
                embed = discord.Embed(title=pollTitle, description="", color=discord.Colour.blue())
                voting_msg = await message.channel.send(embed=embed)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
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
                    '"yes-no" :\n'
                    'Yes-No疑問文を作成します\n'
                    '[CANDIDATE]は必要ありません\n'
                    '"vote" :\n'
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
        embedData.add_field(name = "**$number**", value = "１から１０までの数字のリアクションを追加します")
        embedData.add_field(name = "**$repeat**", value = "BOTは打った文字をオウム返ししてくれます", inline = False)
        embedData.add_field(name = "**$question**", value = "⭕ ❌質問や、多項目の質問を作成します\n詳しくは\"$question help\"で確認できます", inline = False)
        embedData.add_field(name = "**$ping**", value = "BOTのping値を返します", inline = False)
        '''
        embedData.add_field(name = "**$number**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**$number**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**$number**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**$number**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**$number**", value = "ping値を返します", inline = False)
        embedData.add_field(name = "**$number**", value = "ping値を返します", inline = False)
        '''
        embedData.set_thumbnail(url = "https://cdn.discordapp.com/emojis/933926187619733545.webp?size=96&quality=lossless")
        await message.channel.send(embed=embedData)
        return


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
client.run(os.getenv("BOT_TOKEN"))
