from bs4 import BeautifulSoup
import requests
import os
DB_PATH = os.path.dirname(__file__) + '/CoronaBotDB'
def distance_update():
    url = 'https://velog.io/@i-zro/지역-사회적-거리'
    req = requests.get(url)
    html = BeautifulSoup(req.content, 'html.parser')
    target = html.find('div')
    target = target.find('img').get('src')

    f = open(DB_PATH+"/distance.txt", 'w')
    f.write(target)
    f.close()

distance_update()