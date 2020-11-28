from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import datetime
import requests

app = Flask(__name__)


# 서버가 정상적으로 작동하는지 확인하는 임시 코드
@app.route("/")
def hello():
    return "Hello"


class News:
    news_list = []

    def __init__(self):
        self.date = ""
        self.title = ""
        self.link = ""

    @staticmethod
    def create(pub, title, link):
        news = News()
        news.date = pub
        news.title = title
        news.link = link
        News.news_list.append(news)


def get_current_news(TOPIC='코로나 후유증'):
    news_num = 5  # 보여줄 뉴스 개수
    BASE_URL = f'http://newssearch.naver.com/search.naver?where=rss&query={TOPIC}&field=1&nx_search_query=&nx_and_query=&nx_sub_query=&nx_search_hlquery=&is_dts=0'
    data = ''
    result = requests.get(BASE_URL)
    result.encoding = 'UTF-8'
    soup = BeautifulSoup(result.text, 'html.parser')

    items = soup.select('item')

    for item in items[:news_num]:  # 5개 까지만 불러오기
        news = ""
        pub_date = item.select('pubDate')[0].text
        pub_date = datetime.datetime.strptime(pub_date, '%a, %d %b %Y %H:%M:%S %z')
        news = news + f'발행일시 : {pub_date.year}년 {pub_date.month}월 {pub_date.day}일 {pub_date.hour}시 {pub_date.minute}분'
        title = item.select('title')[0].text
        link = str(item).split('<link/>')[1]
        link = link.split('<description>')[0].strip()
        News.create(news, title, link)

    send = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                "title": News.news_list[0].title,
                                "description": News.news_list[0].date,
                                "thumbnail": {
                                    "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자세히 보러가기",
                                        "webLinkUrl": News.news_list[0].link
                                    }
                                ]
                            },
                            {
                                "title": News.news_list[1].title,
                                "description": News.news_list[1].date,
                                "thumbnail": {
                                    "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자세히 보러가기",
                                        "webLinkUrl": News.news_list[1].link
                                    }
                                ]
                            },
                            {
                                "title": News.news_list[2].title,
                                "description": News.news_list[2].date,
                                "thumbnail": {
                                    "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자세히 보러가기",
                                        "webLinkUrl": News.news_list[2].link
                                    }
                                ]
                            },
                            {
                                "title": News.news_list[3].title,
                                "description": News.news_list[3].date,
                                "thumbnail": {
                                    "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자세히 보러가기",
                                        "webLinkUrl": News.news_list[3].link
                                    }
                                ]
                            },
                            {
                                "title": News.news_list[4].title,
                                "description": News.news_list[4].date,
                                "thumbnail": {
                                    "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자세히 보러가기",
                                        "webLinkUrl": News.news_list[4].link
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }
    }

    return send