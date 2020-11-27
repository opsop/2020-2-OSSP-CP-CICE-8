from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import sqlite3, json

# 하루에 한번만 돌아가게

decode_key = unquote(
    'O25gUy60KqtQ%2B0JSuKlerJKpJxLyZNK4OHXqxZArRcQVzeS5iqA3G6jHNJIBiFnHA%2BQPBstl32Ua6zW%2Bc2aQ8Q%3D%3D')
url = 'http://apis.data.go.kr/1741000/DisasterMsg2/getDisasterMsgList'


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


conn = sqlite3.connect("disaster_message_temp.db", isolation_level=None)
conn.execute("CREATE TABLE IF NOT EXISTS MESSAGE \
    (id integer PRIMARY KEY, create_date text, location_name text, msg text)")
conn.execute("DELETE from MESSAGE")
i = 1

d = 0  # 추출할 재난문자 개수
while (d < 300):
    mms = get_emergency_alerts(i)
    # print(i)
    rows = mms['DisasterMsg'][1]['row']
    for idx, row in enumerate(rows):
        _id = (i - 1) * 10 + idx
        row['msg'] = row['msg'].replace('"', "'")

        query = """INSERT INTO MESSAGE(id, create_date, location_name, msg)
                VALUES ( "%d", "%s", "%s", "%s" )""" % (_id, row['create_date'], row['location_name'], row['msg'])
        print(query)
        conn.execute(query)
        d = _id
    i += 1

conn.commit()
conn.close()