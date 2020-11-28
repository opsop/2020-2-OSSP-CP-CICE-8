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
        self.title = ""
        self.link = ""

    @staticmethod
    def create(title, link):
        News.news_list.append(News(title, link))

def get_current_news(TOPIC='코로나 후유증'):
    news_num = 5 # 보여줄 뉴스 개수
    BASE_URL = f'http://newssearch.naver.com/search.naver?where=rss&query={TOPIC}&field=1&nx_search_query=&nx_and_query=&nx_sub_query=&nx_search_hlquery=&is_dts=0'
    data = ''
    result = requests.get(BASE_URL)
    result.encoding = 'UTF-8'
    soup = BeautifulSoup(result.text, 'html.parser')

    items = soup.select('item')

    news = "[ 최신 네이버 뉴스 ]\n"

    for item in items[:news_num]:  # 5개 까지만 불러오기
        pub_date = item.select('pubDate')[0].text
        pub_date = datetime.datetime.strptime(pub_date, '%a, %d %b %Y %H:%M:%S %z')
        news = news + f'\n발행일시 : {pub_date.year}년 {pub_date.month}월 {pub_date.day}일 {pub_date.hour}시 {pub_date.minute}분'
        title = item.select('title')[0].text
        news = news + "\n" + title
        link = str(item).split('<link/>')[1]
        link = link.split('<description>')[0].strip()
        News.create(title, link)
        # news = news + "\n👉" + link
    # news = news + '\n\n📪 관련 주제 뉴스 더보기'
    # url = 'http://search.naver.com/search.naver'
    # param = {
    #     'where': 'news',
    #     'query': TOPIC,
    # }
    #
    # header = {'User-Agent': 'Mozilla/5.0', 'referer': 'http://naver.com'}
    # response = requests.get(url, params=param, headers=header)
    # news = news + '\n' + response.url
    # return news


@app.route('/naver_news', methods=['POST'])
def naver_news():
    body = request.get_json()
    content = body["action"]["detailParams"]["corona_topic"]["value"]
    get_current_news(str(content))
    send = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                {"buttons": [
                                    {
                                        "action": "webLink",
                                        "label": News.news_list[0].title,
                                        "webLinkUrl": News.news_list[0].link
                                    }]},
                                {"buttons": [
                                    {
                                        "action": "webLink",
                                        "label": News.news_list[1].title,
                                        "webLinkUrl": News.news_list[1].link
                                    }]},
                                {"buttons": [
                                    {
                                        "action": "webLink",
                                        "label": News.news_list[2].title,
                                        "webLinkUrl": News.news_list[2].link
                                    }]},
                                {"buttons": [
                                    {
                                        "action": "webLink",
                                        "label": News.news_list[3].title,
                                        "webLinkUrl": News.news_list[3].link
                                    }]},
                                {"buttons": [
                                    {
                                        "action": "webLink",
                                        "label": News.news_list[4].title,
                                        "webLinkUrl": News.news_list[4].link
                                    }]}
                    }]
                }}
        ]
    }
    }
    return jsonify(send)


if __name__ == '__main__':
    app.run(host="0.0.0.0")