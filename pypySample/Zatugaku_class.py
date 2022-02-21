# --------------------------------------------------------------------------------------------------- #
# -----------classをリスト化して、ランダムに取り出して表示させることのできるスクリプトの例です------------ #
# --------------------------------------------------------------------------------------------------- #

import random
class Zatugaku:
    def __init__(self, score, title, description, fromorkinds, url):
        self.score         = score
        self.title         = title
        self.description   = description
        self.fromorkinds   = fromorkinds
        self.url           = url

    def getScore(self):
        return self.score

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getFromorkinds(self):
        return self.fromorkinds

    def getUrl(self):
        return self.url

Zatulist = [Zatugaku(
                    "ホワイトタイガーは正確にはベンガルトラの白変種で、野生では見ることができなくなってしまったほどの珍しさ。",
                    "[トラは狩りの成功率が10%！？]",
                    "->トラの狩りの成功率はわずか10%ほどと、とても低いらしい...\n"+
                    "しかも狩りのチャンスは一日1～2回くらいだとか",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    ),
            Zatugaku(
                    "あの可愛いウサギがまさかの...",
                    "[ウサギは自分のうんこを肛門から直に食べる。]",
                    "->植物だけを食べる動物の胃腸にすむバクテリアは、\n"+
                    "植物を分解することで増え、うんこと一緒に出てくるという。\n"+
                    "ウサギは、これを再び食べることでタンパク質などの栄養をとっているそうだ。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    ),
            Zatugaku(
                    "コアラの主食であるユーカリには、猛毒の青酸やタンニンなどが含まれている。",
                    "[コアラはユーカリにふくまれる猛毒のせいで一日中寝ている。]",
                    "->この毒入りの葉っぱが食べられる体になったことで\n"+
                    "生存競争に勝ち残ったコアラだが、栄養も少なく解毒にエネルギーを費やすため、\n"+
                    "省エネで一日中寝るしかなくなってしまったという。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    ),
            Zatugaku(
                    "あまりにも風が強いと、「明日は明日の風がふくさ」と狩りを諦めてしまう。",
                    "[サーバルは耳がよすぎて狩りができないことがある。]",
                    "->土の中にいるネズミの動きさえ感じとれるほど敏感な耳を持つサーバル。\n"+
                    "しかしビュービューと風が強くふく日はこの武器が仇となり、\n"+
                    "なかなか獲物の居場所が突き止められないことも。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    ),
            Zatugaku(
                    "これが、毛皮の美しさから「森の貴婦人」といわれる由縁だ。",
                    "[オカピの体はオイルでテカテカ。]",
                    "->高温多湿な熱帯雨林にすむため、濡れて体温を下げないよう\n"+
                    "水をはじく油分たっぷりのオイリーな体液を身に纏ったオカピ。\n"+
                    "体はいつもテカり、触るとベトベトするだけでなく茶色の体液がついてしまう。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    ),
            Zatugaku(
                    "約2センチの大きさで生まれたカンガルーの赤ちゃんはすぐにお母さんの袋の中に隠れてしまうため、生まれた日がよく分からない。",
                    "[カンガルーの誕生日はてきとう。]",
                    "->半年ほどお母さんの袋の中で育ち、袋からひょっこり顔を出した日を\n"+
                    "「初顔認知日」としてカンガルーの誕生日としているのだ。",
                    "動物",
                    "https://www.jalan.net/news/article/466810/",
                    )
]

Z = random.choice(Zatulist)
#type(Zatulist))

S = Z.getScore()
T = Z.getTitle()
D = Z.getDescription()
F = Z.getFromorkinds()
U = Z.getUrl()
P = Z.getPoint()

print(Z.getScore())
print(Z.getTitle())
print(Z.getDescription())
print(Z.getFromorkinds())
print(Z.getUrl())
print(Z.getPoint())