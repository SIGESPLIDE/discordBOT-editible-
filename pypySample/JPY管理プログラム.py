合計 = 0
for i in [1, 5, 10, 50, 100, 500, 1000, 2000, 5000, 10000]:
    n =  input(str(i)+"円の枚数を入力してください >> ")

    try:
        if n is '':
            n = 0
        m = int(n)
        合計 += m*i

    except ValueError as e:
            quit(f"エラーが発生したのでプログラムを終了します\nエラー＝{e.args}")

print(f"合計金額は{合計}円です")