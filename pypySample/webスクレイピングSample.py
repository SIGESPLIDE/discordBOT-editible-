# 雑学
import random
import re # 正規表現
import requests # httpResponse
from bs4 import BeautifulSoup # html加工

#request送信
load_url = "https://kurashi-no.jp/I0023637" # 参照URL
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# タイトル一覧入手
titles = []
for element in soup.find_all(class_="c-ttl-article-lv2"):
  # 要らないところを削除
  text = re.sub("^.*?span>|<.*$","",str(element))
  text = re.sub("[⓪①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚㉛㉜㉝㉞㉟㊱㊲㊳㊴㊵㊶㊷㊸㊹㊺㊻㊼㊽㊾㊿]"," ",text)

  # タイトル一覧にappend
  titles.append(text)
# 最後のいらない奴を削除
titles.pop(-1)

# 中身を入手
htmlText = soup.prettify()
texts = []
for element in soup.find_all("p"):
  text = str(element)
  text = re.sub("上記.*?(、|。)","",text)
  # チェック
  if re.search("[0-9]+?個目",text):
    text = re.sub("<p>.*?。|</p>|<br(|/)>\n<br(|/)>","",text)
    texts.append(text)
i = random.randint(0,len(titles))
print(titles[i]+"\n"+texts[i])



#動物
#request送信
load_url = "https://www.jalan.net/news/article/466810/" # 参照URL
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# タイトル一覧入手
titles = []
for element in soup.find_all("h2"):
  text = str(element)
  if re.search("^<h2>(?!\<).*</h2>$",text):
    text = re.sub("<(|/)h2>","",text)
    titles.append(text)

# 中身を入手
htmlText = soup.prettify()
texts = []
for title in titles:
  # チェック
  if re.search("<h2>\n.*?"+title+"(.|\s)*?<h3>",htmlText):
    text = re.search("<h2>\n.*?"+title+"(.|\s)*?<h3>",htmlText).group()
    text = re.sub("<h2>(.|\s)*?</h2>|<(|/)p>|\s*?|<h3>","",text)
    text = re.sub("。","。\n",text)
    texts.append(text)
