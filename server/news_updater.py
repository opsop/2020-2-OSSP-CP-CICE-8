import datetime
from naver_news_db import insert_db, nrefresh_db, crawl_naver
from youtube_db import insert_db, yrefresh_db, crawl_tube

now = datetime.datetime.now()

def n_update():
    naver_up_hour = [9, 13, 18] # 9시, 13시, 18시에 네이버 뉴스 업데이트 예정

    if now.hour in naver_up_hour and now.minute == 0 and now.second == 0:
        nrefresh_db()
        crawl_naver()

def y_update():
    you_up_hour = [9, 13, 18] # 9시, 13시, 18시에 유튜브 뉴스 업데이트 예정

    if now.hour in you_up_hour and now.minute == 0 and now.second == 0:
        yrefresh_db()
        crawl_tube()

def news_update():
    n_update()
    y_update()