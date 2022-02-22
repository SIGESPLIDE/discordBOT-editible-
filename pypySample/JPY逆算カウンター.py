#入力した金額から最大個数がなるべく少なくなるようにそれぞれの金種を割り出す
try:
    money = int(input('計算したい金額を半角数字で入力してください(円)> '))
    try:
        print('金額:',money,'円',sep=' ')
        maisuu = money // 10000
        money = money % 10000
        print('一万円札=',maisuu,'枚',sep=' ')
        maisuu = money // 5000
        money = money % 5000
        print('五千円札=',maisuu,'枚',sep=' ')
        maisuu = money // 1000
        money = money % 1000
        print('千円札　=',maisuu,'枚',sep=' ')
        maisuu = money // 500
        money = money % 500
        print('五百円玉=',maisuu,'枚',sep=' ')
        maisuu = money // 100
        money = money % 100
        print('百円玉　=',maisuu,'枚',sep=' ')
        maisuu = money // 50
        money = money % 50
        print('五十円玉=',maisuu,'枚',sep=' ')
        maisuu = money // 10
        money = money % 10
        print('十円玉　=',maisuu,'枚',sep=' ')
        maisuu = money // 5
        money = money % 5
        print('五円玉　=',maisuu,'枚',sep=' ')
        print('一円玉　=',money,'枚',sep=' ')
    except Exception as e:
        print(e.arg)
except ValueError:
    print("エラー。数字以外の文字を検知しました。初めからやり直してください")