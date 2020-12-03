# from pytchat import LiveChat
import pafy
import pandas as pd
import requests
import html

search_word = '코로나'
search_word = search_word+'뉴스'
youtube_key = "AIzaSyDgTuKL86WcF3uS6b6gBWEUoaUdd_cAOOA"
news_num = 5
r = requests.get(f"https://www.googleapis.com/youtube/v3/search?part=snippet&key={youtube_key}&q={search_word}19&maxResults={news_num}")
j = r.json()

if list(j.keys())[0] != "error":
    for i in j['items']:
        print(html.unescape(i['snippet']['title']))
        print(html.unescape(i['snippet']['description']))
        print(i['snippet']['thumbnails']['high']['url'])
        print(f"https://www.youtube.com/watch?v={i['id']['videoId']}")
# item_list = []
# j = j['items']
# print(j)