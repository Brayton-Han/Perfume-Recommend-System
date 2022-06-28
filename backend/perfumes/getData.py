#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import django
import sys
sys.path.append('C:/Users/dell/Desktop/Expert_System/backend')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()
from perfumes.models import Perfume
import requests
from bs4 import BeautifulSoup

Headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

def download_page(tar):
    print("Downloading " + tar)
    requests.packages.urllib3.disable_warnings()
    html = requests.get(tar, headers=Headers, verify=False)
    return html

def paser_html(html, rank, smells):
    soup = BeautifulSoup(html.content, 'lxml')
    name = soup.find_all("h1")[0].string
    print(name)
    img = "https:" + soup.find_all("img", class_='noxx')[0]["src"]
    fileurl = "C:/Users/dell/Desktop/Expert_System/imgs/" + str(rank) + ".png"
    r = requests.get(img)
    with open(fileurl, 'wb') as f:
        f.write(r.content)
    info = soup.find_all("ul", class_='item_info')[0].get_text(strip=True, separator='\n').splitlines()
    brand = info[1]
    print(brand)
    type_ = info[3]
    print(type_)
    m = info.index('属性：')
    n = info.index('标签：')
    attr = info[m + 1]
    print(attr)
    creater = info[n - 1]
    print(creater)
    labels = info[n + 1:]
    print(labels)
    rate = soup.find_all("div", class_='score')[0].string
    print(rate)
    time = soup.find_all("div", class_='inbar')[5]["style"][29:31]
    print(time)
    if info[4] == "前调：":
        i = info.index('前调：')
        j = info.index('中调：')
        k = info.index('后调：')
        pre = info[i + 1: j]
        mid = info[j + 1: k]
        after = info[k + 1: m]
        print(pre)
        print(mid)
        print(after)

        Perfume.objects.create(rank=rank, name=name, img=fileurl, brand=brand, style=type_, top=" ".join(pre), 
                               middle=" ".join(mid), base=" ".join(after), attr=attr, creater=creater, 
                               labels=" ".join(labels), rate=float(rate), time=int(time), smell_1=smells[0], 
                               smell_2=smells[1], smell_3=smells[2], smell_4=smells[3])
    else:
        smell = info[5:m]
        print(smell)
        Perfume.objects.create(rank=rank, name=name, img=fileurl, brand=brand, style=type_, smells=" ".join(smell), 
                               attr=attr, creater=creater, labels=" ".join(labels), rate=float(rate), time=int(time), 
                               smell_1=smells[0], smell_2=smells[1], smell_3=smells[2], smell_4=smells[3])
    if len(smells) == 5:
        Perfume.objects.filter(rank=rank).update(smell_5=smells[4])

def main():
    rank = 140
    for i in range(8, 11):
        target = 'https://www.nosetime.com/top200.php?type=trade&page=' + str(i) + '#list'
        html = download_page(target)
        soup = BeautifulSoup(html.content, 'lxml')
        xs = soup.find_all("div", class_='trade-article fr')
        for item in xs:
            rank += 1
            smells = item.find_all("div", class_='sharp-taste clearfloat')[0].get_text(strip=True, separator="\n").splitlines()[1:]
            print(smells)
            url = 'https://www.nosetime.com' + item.find_all("a")[0]["href"]
            paser_html(download_page(url), rank, smells)
            print('\n')

if __name__ == '__main__':
	main()
