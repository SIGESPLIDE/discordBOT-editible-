_1yen, _5yen, _10yen, _50yen, _100yen, _500yen, _1000yen, _2000yen, _5000yen, _10000yen = 1, 5, 10, 50, 100, 500, 1000, 2000, 5000, 10000,
JPYdict = {_1yen:0, _5yen:0, _10yen:0, _50yen:0, _100yen:0, _500yen:0, _1000yen:0, _2000yen:0, _5000yen:0, _10000yen:0}

in1yen = input("1円玉の枚数を入れてください")
if in1yen is None:
    in1yen = 0
JPYdict.update({_1yen:in1yen})
in5yen = input("5円玉の枚数を入れてください")
if in5yen is None:
    in5yen = 0
JPYdict.update({_5yen:in5yen})
in10yen = input("10円玉の枚数を入れてください")
if in10yen is None:
    in10yen = 0
JPYdict.update({_10yen:in10yen})
in50yen = input("50円玉の枚数を入れてください")
if in50yen is None:
    in50yen = 0
JPYdict.update({_50yen:in50yen})
in100yen = input("100円玉の枚数を入れてください")
if in100yen is None:
    in100yen = 0
JPYdict.update({_100yen:in100yen})
in500yen = input("500円玉の枚数を入れてください")
if in500yen is None:
    in500yen = 0
JPYdict.update({_500yen:in500yen})
in1000yen = input("1000円札の枚数を入れてください")
if in1000yen is None:
    in1000yen = 0
JPYdict.update({_1000yen:in1000yen})
in2000yen = input("2000円札の枚数を入れてください")
if in2000yen is None:
    in2000yen = 0
JPYdict.update({_2000yen:in2000yen})
in5000yen = input("5000円札の枚数を入れてください")
if in5000yen is None:
    in5000yen = 0
JPYdict.update({_5000yen:in5000yen})
in10000yen = input("10000円札の枚数を入れてください")
if in10000yen is None:
    in10000yen = 0
JPYdict.update({_10000yen:in10000yen})

合計 = JPYdict.get(_1yen)*_1yen + JPYdict.get(_5yen)*_5yen + JPYdict.get(_10yen)*_10yen + JPYdict.get(_50yen)*_50yen + JPYdict.get(_100yen)*_100yen + JPYdict.get(_500yen)*_500yen + JPYdict.get(_1000yen)*_1000yen + JPYdict.get(_2000yen)*_2000yen + JPYdict.get(_5000yen)*_5000yen + JPYdict.get(_10000yen)*_10000yen
if 合計 == 0 or 合計 is None:
    合計 = 0
    print("合計金額は、「0円」です。")
else:
    print(f"合計金額は、「{合計}円」です。")