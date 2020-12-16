from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import sqlite3, json
from ConstVar import DB_PATH
msg_num = 300  # 한번 업데이트할 때마다 최신순으로 300개씩 가져오기
page_num = 10  # 한번 가져올 때 최대로 가져올 수 있는 재난 문자 개수
i = 1  # 공공데이터포털 데이터에서 페이지 넘버 (i를 1씩 증가시키면서 재난 문자를 10개(page_num)씩 가져옴)
init = 1  # 초기 페이지 넘버(제일 첫 페이지)
d = 0  # 추출할 재난문자 개수

# 하루에 한번 업데이트

decode_key = unquote('O25gUy60KqtQ%2B0JSuKlerJKpJxLyZNK4OHXqxZArRcQVzeS5iqA3G6jHNJIBiFnHA%2BQPBstl32Ua6zW%2Bc2aQ8Q%3D%3D') # 개인키 값
url = 'http://apis.data.go.kr/1741000/DisasterMsg2/getDisasterMsgList'  # 공공데이터포털 주소


def info_parser(content):
    return content['DisasterMsg']


def get_emergency_alerts(page_number):
    queryParams = '?' + urlencode(
        {quote_plus('ServiceKey'): decode_key, quote_plus('pageNo'): page_number, quote_plus('numOfRows'): '10',
         quote_plus('type'): 'json', quote_plus('flag'): 'Y'})   # 공공데이터포털에서 제공한 API를 받아오는 형식
    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    # response_body = urlopen(request).read()
    resource = urlopen(request)
    content = resource.read().decode(resource.headers.get_content_charset())
    dict_content = json.loads(content)
    return dict_content

try:
    #conn = sqlite3.connect("disaster_message_temp.db", isolation_level=None)
    conn = sqlite3.connect(DB_PATH + "/disaster_message_temp.db", isolation_level=None)

    conn.execute("CREATE TABLE IF NOT EXISTS MESSAGE \
        (id integer UNIQUE, create_date text, location_name text, msg text)")
    conn.execute("DELETE from MESSAGE")

    # i : 공공데이터포털 데이터에서 페이지 넘버 (i를 1씩 증가시키면서 재난 문자를 10개(page_num)씩 가져옴)
    # init : 초기 페이지 넘버(제일 첫 페이지)
    # d: 추출할 재난문자 개수
    while (d < msg_num):
        mms = get_emergency_alerts(i)

        rows = mms['DisasterMsg'][1]['row']  # 데이터의 mms['DisasterMsg'][1]['row']에 필요한 정보가 있음.
        for idx, row in enumerate(rows):
            _id = (i - init) * page_num + idx   # _id 로 DB 내의 index 값 설정
            row['msg'] = row['msg'].replace('"', "'")

            query = """INSERT OR REPLACE INTO MESSAGE(id, create_date, location_name, msg)
                    VALUES ( "%d", "%s", "%s", "%s" )""" % (_id, row['create_date'], row['location_name'], row['msg'])
            #print(query)
            conn.execute(query)
            d = _id
        i += 1

finally:
    conn.commit()
    conn.close()
