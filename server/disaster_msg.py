from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import sqlite3, json
from ConstVar import DB_PATH
msg_num = 300 # 한번 업데이트할 때마다 최신순으로 300개씩 가져오기

# 하루에 한번만 돌아가게

decode_key = unquote(
    'O25gUy60KqtQ%2B0JSuKlerJKpJxLyZNK4OHXqxZArRcQVzeS5iqA3G6jHNJIBiFnHA%2BQPBstl32Ua6zW%2Bc2aQ8Q%3D%3D')
url = 'http://apis.data.go.kr/1741000/DisasterMsg2/getDisasterMsgList'  # 공공데이터포털 주소


def info_parser(content):
    return content['DisasterMsg']


def get_emergency_alerts(page_number):
    queryParams = '?' + urlencode(
        {quote_plus('ServiceKey'): decode_key, quote_plus('pageNo'): page_number, quote_plus('numOfRows'): '10',
         quote_plus('type'): 'json', quote_plus('flag'): 'Y'})
    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    # response_body = urlopen(request).read()
    resource = urlopen(request)
    content = resource.read().decode(resource.headers.get_content_charset())
    dict_content = json.loads(content)
    return dict_content

#conn = sqlite3.connect("disaster_message_temp.db", isolation_level=None)
conn = sqlite3.connect(DB_PATH + "/disaster_message_temp.db", isolation_level=None)

conn.execute("CREATE TABLE IF NOT EXISTS MESSAGE \
    (id integer PRIMARY KEY, create_date text, location_name text, msg text)")
conn.execute("DELETE from MESSAGE")

i = 1  # 공공데이터포털 데이터에서 페이지 넘버
d = 0  # 추출할 재난문자 개수
while (d < msg_num):
    mms = get_emergency_alerts(i)
    # print(i)
    rows = mms['DisasterMsg'][1]['row']  # 데이터의 mms['DisasterMsg'][1]['row']에 필요한 정보가 있음.
    for idx, row in enumerate(rows):
        _id = (i - 1) * 10 + idx   # 한 페이지마다 10개씩있고 한번 가져올때 한페이지만 가져올 수 있음.
        row['msg'] = row['msg'].replace('"', "'")

        query = """INSERT INTO MESSAGE(id, create_date, location_name, msg)
                VALUES ( "%d", "%s", "%s", "%s" )""" % (_id, row['create_date'], row['location_name'], row['msg'])
        #print(query)
        conn.execute(query)
        d = _id
    i += 1

conn.commit()
conn.close()
