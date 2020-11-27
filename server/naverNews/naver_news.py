from datetime import datetime
import requests
from bs4 import BeautifulSoup

'''
네이버 뉴스 보기 기능의 기본이 되는 파이썬 함수
챗봇에서 사용할 수 있도록 바꿔줄 것
'''

def get_current_news(TOPIC = input()):
    BASE_URL = f'http://newssearch.naver.com/search.naver?where=rss&query={TOPIC}&field=1&nx_search_query=&nx_and_query=&nx_sub_query=&nx_search_hlquery=&is_dts=0'
    data = ''
    result = requests.get(BASE_URL)
    result.encoding = 'UTF-8'
    soup = BeautifulSoup(result.text, 'html.parser')

    items = soup.select('item')

    print("[ 최신 네이버 뉴스 ]")

    for item in items[:5]: # 5개 까지만 불러오기
        pub_date = item.select('pubDate')[0].text
        pub_date = datetime.strptime(pub_date, '%a, %d %b %Y %H:%M:%S %z')
        print(f'\n발행일시 : {pub_date.year}년 {pub_date.month}월 {pub_date.day}일 {pub_date.hour}시 {pub_date.minute}분')
        title = item.select('title')[0].text
        print(title)
        link = str(item).split('<link/>')[1]
        link = link.split('<description>')[0].strip()
        print("👉",link)

    print('\n📪 관련 주제 뉴스 더보기')
    url = 'http://search.naver.com/search.naver'
    param = {
        'where': 'news',
        'query': TOPIC,
    }

    header = {'User-Agent': 'Mozilla/5.0', 'referer': 'http://naver.com'}
    response = requests.get(url, params=param, headers=header)
    print(response.url)

get_current_news()
