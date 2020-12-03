import requests
import json
import datetime
import html

def get_current_news(search_word = '코로나'):
    client_id = "BMMCxLy7yJWCna0lxGcL" # 취득한 아이디 넣기
    client_secret = "2tVAp55OCM"  # 취득한 키 넣기
    encode_type = 'json'
    max_display = 5
    sort = 'date'
    start = 1
    search_word.replace(' ','+')

    url = f"https://openapi.naver.com/v1/search/news.{encode_type}?query={search_word}&display={str(int(max_display))}&start={str(int(start))}&sort={sort}"

    headers = {'X-Naver-Client-Id' : client_id,
               'X-Naver-Client-Secret': client_secret
               }

    r = requests.get(url, headers = headers)
    j = json.loads(r.text)

    news_add = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_word}'

    item_list = []
    for idx, i in enumerate(j['items']):
        pub_date = datetime.datetime.strptime(i['pubDate'], '%a, %d %b %Y %H:%M:%S %z')
        date = f'발행일시 : {pub_date.year}년 {pub_date.month}월 {pub_date.day}일 {pub_date.hour}시 {pub_date.minute}분'
        title = html.unescape(i['title']).replace("<b>", "").replace("</b>", "")

        img_url = f'https://openapi.naver.com/v1/search/image.{encode_type}?query={title}&display={str(1)}'
        r_img = requests.get(img_url, headers = headers)
        j_img = json.loads(r_img.text)
        thumb = ""
        for k in j_img['items']:
            thumb = k['link']
        if thumb == "":
            thumb = "https://image.dongascience.com/Photo/2020/01/008f1295bea0e575bdb0d8fcdd1a7390.jpg"
        item_list.append({
                                    "title": title,
                                    "description": date,
                                    "thumbnail": {
                                        "imageUrl": thumb},
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "자세히 보러가기",
                                            "webLinkUrl": i['link']
                                        }
                                    ]
                                })

    addition = {
        "title": search_word.replace("+", " ") + " 관련 주제가 더 보고 싶으시다면❓",
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

    item_list.append(addition)

    send = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": item_list}}]}}

    return send

# def search(TOPIC='코로나'):
#     news_add = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={TOPIC}'
#     return news_add
#
# def exc():
#     send = {
#         "version": "2.0",
#         "template": {
#             "outputs": [
#                 {
#                     "simpleText": {
#                         "text": search()
#                     }
#                 }
#             ]
#         }
#     }
#     return send
