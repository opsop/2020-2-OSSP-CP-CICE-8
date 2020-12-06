from bs4 import BeautifulSoup
import requests
import os
DB_PATH = os.path.dirname(__file__) + '/CoronaBotDB'

headers={
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'
}

def distance_update():
    url = 'https://velog.io/@i-zro/지역-사회적-거리'
    req = requests.get(url, headers = headers)
    html = BeautifulSoup(req.content, 'html.parser')
    target = html.find('div')
    target = target.find('img').get('src')

    if target == "":
        pass
    else:
        f = open(DB_PATH+"/distance.txt", 'w')
        f.write(target)
        f.close()
