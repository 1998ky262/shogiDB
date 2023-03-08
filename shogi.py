import requests
from bs4 import BeautifulSoup
import time
n =int(input("何番目の棋士番号から出力しますか？"))
for i in range(n, 335):
    if not i==239:
       url = f"https://www.shogi.or.jp/player/pro/{i}.html"
       r = requests.get(url)
       soup = BeautifulSoup(r.content.decode('utf-8', 'replace'), "html.parser")
       jp_element = soup.find("span", class_="jp")
       jp_text = jp_element.get_text()
       print(str(i)+jp_text)
    time.sleep(1)

print("終了")