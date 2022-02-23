# --------------------------------------------------------------------------------------------------- #
# -----------classをリスト化して、ランダムに取り出して表示させることのできるスクリプトの例です------------ #
# --------------------------------------------------------------------------------------------------- #

import random

class Zatugaku:
    def __init__(self, score, title, description, fromorkinds, url, thumbnail, point):
        for key,value in locals().items():
            if not key == "self":
                self.__dict__[key] = value

Zatulist = [Zatugaku(
                    "スコアです",
                    "タイトルです",
                    "詳細です",
                    "分類です",
                    "URLです",
                    "サムネです",
                    "ポイントです"
                    )
]

data = random.choice(Zatulist)
print(data.score,data.title,data.description,data.fromorkinds,data.url,data.thumbnail,data.point, sep="\n")