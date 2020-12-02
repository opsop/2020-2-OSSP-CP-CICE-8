from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import datetime
import requests
import urllib.request
import ssl

app = Flask(__name__)


# 서버가 정상적으로 작동하는지 확인하는 임시 코드
@app.route("/")
def hello():
    return "Hello"


class News:
    news_list = []

    def __init__(self):
        self.image_url = ""
        self.date = ""
        self.title = ""
        self.link = ""

    @staticmethod
    def create(img, pub, title, link):
        news = News()
        news.image_url = img
        news.date = pub
        news.title = title
        news.link = link
        News.news_list.append(news)

    @staticmethod
    def refresh():
        News.news_list = []


def search(TOPIC='코로나'):
    news_add = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={TOPIC}'
    return news_add


def get_current_news(TOPIC='코로나 후유증'):
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.set_ciphers('HIGH:!DH:!aNULL')
    context.set_ciphers('DEFAULT@SECLEVEL=1')
    News.refresh()
    headers = {'User-Agent': 'Mozilla/5.0'}
    news_num = 5  # 보여줄 뉴스 개수
    img_show = 4  # 이미지 파싱해서 몇번째에서 뉴스 이미지 가져올지
    BASE_URL = f'http://newssearch.naver.com/search.naver?where=rss&query={TOPIC}&field=1&nx_search_query=&nx_and_query=&nx_sub_query=&nx_search_hlquery=&is_dts=0'
    topic = TOPIC.replace(' ', '+')
    news_add = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={topic}'
    result = requests.get(BASE_URL, verify = False, headers = headers)
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

        html_req = urllib.request.Request(link, headers=headers)
        html = urllib.request.urlopen(html_req)
        soup = BeautifulSoup(html, "html.parser")
        soup = soup.find_all("img")
        try:
            img = soup[img_show].get('src')
        except:
            img = "https://img1.daumcdn.net/thumb/R720x0/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fliveboard%2Fh21%2F946bac8f3dec4440aa6412140cdeb90b.JPG"

        if img == "":
            img = "https://img1.daumcdn.net/thumb/R720x0/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fliveboard%2Fh21%2F946bac8f3dec4440aa6412140cdeb90b.JPG"
        News.create(img, news, title, link)
    print(news_add)
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
                                    "imageUrl": News.news_list[0].image_url},
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
                                    "imageUrl": News.news_list[1].image_url
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
                                    "imageUrl": News.news_list[2].image_url
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
                                    "imageUrl": News.news_list[3].image_url
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
                                    "imageUrl": News.news_list[4].image_url
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자세히 보러가기",
                                        "webLinkUrl": News.news_list[4].link
                                    }
                                ]
                            },
                            {
                                "title": TOPIC + " 관련 주제가 더 보고 싶으시다면❓",
                                "description": "아래 '보러가기'를 클릭해 주세요❗",
                                "thumbnail": {
                                    "imageUrl": "https://user-images.githubusercontent.com/48379869/100522762-b09d2c00-31ee-11eb-80ee-4716dc3d775f.png"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "보러가기",
                                        "webLinkUrl": news_add
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

# print(get_current_news())

def exc():
    send = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": search()
                    }
                }
            ]
        }
    }
    return send