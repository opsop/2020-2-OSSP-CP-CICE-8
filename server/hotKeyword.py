import sqlite3 as sl
import os
from variable import *


# counting hotKeyword
# from hotKeyword import *
# updateKeyword ( str )
def hotKeyword( nttpass : str ):

        # 테이블 생성
        # 테이블에 nttpass 존재 확인
        # 존재하면 +1 UPDATE
        # 없으면 INSERT data

    try:
        conn = sl.connect(DB_PATH + "/corona.db")
        cur = conn.cursor()

        # insert if not exists
        InsertOrIgnore = f""" INSERT OR IGNORE INTO HOTKEYWORD ( KEYWORD , COUNTING )
                            VALUES ('{nttpass}', 0) """

        # or like this query
        #INSERT INTO tablename(values)
        #SELECT values
        #WHERE NOT EXISTS(SELECT 1 FROM tablename WHERE condition);

        # 인기 키워드 카운팅 update COUNTING
        update = f"""UPDATE HOTKEYWORD SET COUNTING = COUNTING + 1 WHERE KEYWORD='{nttpass}' """

        #테이블 생성
        #query from variable.py
        #cur.execute(QCT_hotKeyword)

        cur.execute(InsertOrIgnore)
        cur.execute(update)
        print(cur.execute("SELECT * FROM HOTKEYWORD").fetchone())


    except Exception as e:
        print(e)

    finally :
        conn.commit()
        cur.close()
        conn.close()

def searchHotKeyword(body):

    # 인기 키워드 로직 채워넣기
    # COUNTING 순으로 정렬 limit 3

    #오는 request 형식 확인
    print(body)
    return dataSendSimple("인기 키워드 테스트중")


print(searchHotKeyword(" "))
