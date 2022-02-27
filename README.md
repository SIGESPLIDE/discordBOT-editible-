# SIGES BOT取扱説明書

開発環境:rpi4(8gb) python v3.7.3
必要用件:python v3.7.3

## -必要permission-

OAuth2:

```bash
BOT
```

Bot:

```css
General
| View Channels
Text
| Send Messages
| Embed Links
| Read Message History
| Use External Emojis
| Add Reactions
```

## -起動-

```text
DISCORD_BOT_TOKEN=<YOUR BOT TOKEN>
python3 discordbot.py
```

## -botｺﾏﾝﾄﾞ-

##### ※コマンドの文頭には、必ず半角の 「 $ 」 が入ります

```mermaid
graph LR
    main>"<h2>メインコマンド</h2>"]
    mainfo(基本コマンド)
    main0[(BOT情報)]---main1
    main0---main2
    main1[使用可能コマンドを確認できます]-->help{"<h3>＄help</h3>"}
    main2[SIGES BOTの各種情報を表示します]-->info{"<h3>＄info</h3>"}

```

```mermaid
graph LR
    z["↓　　↓　　↓　　↓　　↓　　↓<br>※四則演算の計算時に入れる値の数に制限はありません<br>↓　　↓　　↓　　↓　　↓　　↓<br>"]
```

```mermaid
graph TD
    A[(四則演算)]
    B[ｘとｙの]

    a{"＄"addition}
    b{"＄"substraction}
    c{"＄"multiply}
    d{"＄"division}
        a'{"＄"add}
        b'{"＄"sub}
        c'{"＄"mul}
        d'{"＄"div}

    a -- OR --- a'
    b -- OR --- b'
    c -- OR --- c'
    d -- OR --- d'

    B-->2((加算))-->a
    B-->3((減算))-->b
    B-->4((乗算))-->c
    B-->5((除算))-->d
    A ==> B
    A ==> y

    x{"＄eval"}
    y(eval関数を使用します)
    y---->x
```

```mermaid
graph LR
    C[(機能コマンド)]
    e{"＄"splityen}
    f{"＄"combineyen}
    g{"＄"$question}
    h{"＄"zatugaku}
        e'{"＄"spy}
        f'{"＄"com}
        g'{"＄"que}
        h'{"＄"zatu}

    i["入力金額から金種(硬貨や札の種類)を分類します<br>※日本円限定"]
    j["入力された各金種の枚数から合計金額を算出します"]
    k["⭕ ❌質問や、**複数選択肢**の質問を作ることができます<br>※詳しくは`$question help`で確認できます"]
    l["雑学リストを表示します"]

    e -- "OR" --- e'
    f -- "OR" --- f'
    g -- "OR" --- g'
    h -- "OR" --- h'

    e --- i
    f --- j
    g --- k
    h --- l

    C ====> e
    C ====> f
    C ====> g
    C ====> h
```

```mermaid
graph LR
    sub>"<h2>　サブコマンド　</h2>"]
    m{"＄"repeat}
    n{"＄"greet}
    o{"＄"nuber}
    p{"＄"ping}
    q{"＄"yattaze}
    r{"＄"omikuji}
    s{"＄"cat}
        m'["\の後ろの文章をBOTが繰り返します。<br>SIGES BOTメッセージ削除権限がある場合、送信者のメッセージを削除する機能も付いています"]
        n'["あいさつしましょう！"]
        o'["１～１０までの数字のリアクションを追加します"]
        p'["pong"]
        q'["やったぜ"]
        r'["おみくじを引きます"]
        s'["ﾈｺ"]
    m --> m'
    n --> n'
    o --> o'
    p --> p'
    q --> q'
    r --> r'
    s --> s'
```

## `!!!メンテナンス中!!!`

None

## -実装予定・実装するかも-

`$list` :ユーザー毎、チャンネル毎、サーバー毎のリストを作成し、辞書をつくる
