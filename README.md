# SIGES BOT取扱説明書
開発環境:rpi4(8gb) python v3.7.3
必要用件:python v3.7.3

## -必要permission-  
OAuth2:  
```
BOT
```
Bot:  
```
General
 View Channels
Text
 Send Messages
 Embed Links
 Read Message History
 Use External Emojis
 Add Reactions
```
招待リンク `https://discord.com/api/oauth2/authorize?client_id=<Your Bot Application ID>&permissions=271666256&scope=bot`  
  
## -起動-  
```
DISCORD_BOT_TOKEN=<YOUR BOT TOKEN>
python3 discordbot.py
```
  
## -botｺﾏﾝﾄﾞ-  
### TTS関連  
`$add a b `:aとbを加算します
`$cat`:ﾈｺ
`$division a b`:aとbを除算します
`$greet`:あいさつしましょう！
`$help`:使用可能コマンドを確認できます
`$info`:SIGES BOTの各種情報を表示します
`$multiply a b`:aとbの掛け算をします
`$omikuji`:おみくじ
`$ping`:pong
`$yattaze`:やったぜ