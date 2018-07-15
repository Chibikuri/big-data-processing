#!/usr/bin/python
#-*- Doding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
import datetime as dt
from datetime import timedelta

url = "http://www1.river.go.jp/cgi-bin/DspWaterData.exe?KIND=1&ID=307111287708050&BGNDATE=20180614&ENDDATE=20180713&KAWABOU=NO"

req1 = requests.get(url)
soup1 = BeautifulSoup(req1.text, 'lxml')
url = "http://www1.river.go.jp" + soup1.find("iframe")["src"]

req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')
tag_list = []
tags = []
for i in soup.find_all("td"):
    tag_list.append(i.text)

for j in tag_list:
    j = j.strip("\u3000")
    if j == "24:00":
        j = "0:00"
    tags.append(j)

print(tags)
t = 0
with open("test.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["年月日時", "水位"])
    while t < len(tags) - 2:
        tags[t] = dt.datetime.strptime(tags[t], '%Y/%m/%d')
        if tags[t+1] == "0:00":
            tags[t] = tags[t] + timedelta(days=1)
        tags[t] = str(tags[t]).replace("00:00:00", "")
        if tags[t+2] == "閉局":
            tags[t+2] = 0.1
            t = t + 3
        else:
            date = tags[t] + " " + tags[t+1]
            dates = dt.datetime.strptime(date, '%Y-%m-%d %H:%M')
            writer.writerow([dates, float(tags[t+2])])
            t = t + 3
