import requests
import html

def you_news(search_word):
    search_word = search_word['action']['detailParams']
    search_word = search_word['youtube']['value']
    search_word = search_word+'뉴스'
    youtube_key = "AIzaSyDgTuKL86WcF3uS6b6gBWEUoaUdd_cAOOA"
    news_num = 5
    r = requests.get(f"https://www.googleapis.com/youtube/v3/search?part=snippet&key={youtube_key}&q={search_word}19&maxResults={news_num}")
    j = r.json()
    item_list = []
    if list(j.keys())[0] != "error":
        for i in j['items']:
            item_list.append({
                                    "title": html.unescape(i['snippet']['title']),
                                    "description": html.unescape(i['snippet']['description']),
                                    "thumbnail": {
                                        "imageUrl": i['snippet']['thumbnails']['high']['url']},
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "자세히 보러가기",
                                            "webLinkUrl": f"https://www.youtube.com/watch?v={i['id']['videoId']}"
                                        }
                                    ]
                                })

        send = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": item_list}}]}}
    return send