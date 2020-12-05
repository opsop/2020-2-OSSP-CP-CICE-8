import datetime
from naver_news_db import insert_db, nrefresh_db, crawl_naver
from youtube_db import insert_db, yrefresh_db, crawl_tube

now = datetime.datetime.now()

def n_update():
    nrefresh_db()
    crawl_naver()

def y_update():
    yrefresh_db()
    crawl_tube()

def news_update():
    n_update()
    y_update()