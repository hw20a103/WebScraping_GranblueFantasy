from asyncore import write
from unicodedata import name
import re
import csv
import requests
from bs4 import BeautifulSoup

url = "https://xn--bck3aza1a2if6kra4ee0hf.gamewith.jp/article/show/29566"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

tips = soup.select_one('.gbf-pickup_table')
tips2 = tips.find_all('td')
events = []

for i in range(len(tips2)):
    temp = ["","",""]
    #イベント名
    temp[0] = tips2[i].select_one('.gbf-table_center').text
    day = tips2[i].select_one('.bolder').text.split('～')
    #イベント開始日
    #開始日をYYYY/MM/DDの形式に変換
    day_num = re.findall(r'\d+',day[0])
    day0 = str("2022/"+day_num[0]+"/"+day_num[1])
    temp[1] = day0
    #イベント終了日
    #終了日をYYYY/MM/DDの形式に変換
    day_num = re.findall(r'\d+',day[1])
    day1 = str("2022/"+day_num[0]+"/"+day_num[1])
    temp[2] = day1
    events.append(temp)

mat = [
    [111, 222, 333],
    ['aaa', 'bb,bb', 'ccc'],
]



with open('test.csv', 'wt', encoding='utf-8', newline='') as fout:
    # ライター（書き込み者）を作成
    writer = csv.writer(fout)

    writer.writerow(['Subject','Start date','End Date'])

    # ライターでデータ（行列）をファイルに出力
    writer.writerows(events)
    

print(events)