import sqlite3
import requests
import json
import datetime
import html
import os

DB_PATH = os.path.dirname(__file__) + '/CoronaBotDB'


def insert_db(data):
    con = sqlite3.connect(DB_PATH + '/naver.db')
    cursor = con.cursor()
    for row in data:
        cursor.execute("INSERT INTO NEWS VALUES(?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4]))
        con.commit()
    con.close()


def refresh_db():
    con = sqlite3.connect(DB_PATH+'/naver.db')
    con.execute("DELETE FROM NEWS").rowcount
    con.commit()
    con.close()


def crawl_naver():
    client_id = "BMMCxLy7yJWCna0lxGcL"  # 취득한 아이디 넣기
    client_secret = "2tVAp55OCM"  # 취득한 키 넣기
    encode_type = 'json'
    max_display = 5
    sort = 'date'
    start = 1
    search_list = ['코로나 확진자', '코로나 백신', '코로나 후유증']
    add_list = [] # db에 저장할 아이템들

    for i in search_list:
        url = f"https://openapi.naver.com/v1/search/news.{encode_type}?query={i.replace(' ','+')}&display={str(int(max_display))}&start={str(int(start))}&sort={sort}"

        headers = {'X-Naver-Client-Id': client_id,
                   'X-Naver-Client-Secret': client_secret
                   }

        r = requests.get(url, headers=headers)
        j = json.loads(r.text)

        for idx, item in enumerate(j['items']):
            pub_date = datetime.datetime.strptime(item['pubDate'], '%a, %d %b %Y %H:%M:%S %z')
            date = f'발행일시 : {pub_date.year}년 {pub_date.month}월 {pub_date.day}일 {pub_date.hour}시 {pub_date.minute}분'
            title = html.unescape(item['title']).replace("<b>", "").replace("</b>", "")

            img_url = f'https://openapi.naver.com/v1/search/image.{encode_type}?query={title}&display={str(1)}'
            r_img = requests.get(img_url, headers=headers)
            j_img = json.loads(r_img.text)
            thumb = ""
            for k in j_img['items']:
                thumb = k['link']
            if thumb == "":
                thumb = "https://image.dongascience.com/Photo/2020/01/008f1295bea0e575bdb0d8fcdd1a7390.jpg"
            add_list.append([i, title, date, thumb, item['link']])

    insert_db(add_list)

refresh_db()
crawl_naver()