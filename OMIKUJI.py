#randomモジュールをインポート
import random

#listを作る
OmikujiList = ['大吉', '吉', '中吉', '小吉', '半吉', '末吉', '末小吉', '平', '凶', '小凶', '半凶', '末凶', '大凶']

#listの中身をランダムに取得
print("あなたの運勢は"+random.choice(OmikujiList)+"です")
