import sqlite3 as sl
import os
from ConstVar import *
import traceback

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

        # 테이블 생성
        #cur.execute(QCT_hotKeyword)

        # insert if not exists
        """ INSERT OR IGNORE INTO HOTKEYWORD ( KEYWORD , COUNTING )
        VALUES ('{nttpass}', 0) """

        # or like this query
        InsertOrIgnore = f"""INSERT INTO  HOTKEYWORD( KEYWORD , COUNTING ) SELECT '{nttpass}',0
        WHERE NOT EXISTS(SELECT 1 FROM HOTKEYWORD WHERE KEYWORD = '{nttpass}');"""

        # 인기 키워드 카운팅 update COUNTING
        update = f"""UPDATE HOTKEYWORD SET COUNTING = COUNTING + 1 WHERE KEYWORD='{nttpass}' """

        #테이블 생성
        #query from variable.py
        #cur.execute(QCT_hotKeyword)

        cur.execute(InsertOrIgnore)
        cur.execute(update)
        #print(cur.execute("SELECT * FROM HOTKEYWORD").fetchone())


    except Exception as e:
        print("ERROR : " + e)
        print(traceback.format_exc())
    finally :
        conn.commit()
        cur.close()
        conn.close()

def searchHotKeyword(body):

    # 인기 키워드 로직 채워넣기
    # COUNTING 순으로 정렬 limit 3
    res = "인기키워드 테스트중"
    try:
        conn = sl.connect(DB_PATH + "/corona.db")
        # 내림차순 3개까지
        a = conn.execute(" SELECT * FROM HOTKEYWORD ORDER BY COUNTING DESC LIMIT 3 ").fetchall()
        a = list(a)

        rank = ['🥇','🥈','🥉']
        #ex) 1. a \n 2. b \n 3. c
        res = "\n\n".join( i +" : " + str(x[0]) for i,x in zip(rank,a))

    except Exception as e:
        print("ERROR : " + e)
        print(traceback.format_exc())
    finally:
        conn.close()

    #오는 request 형식 확인
    print("인기키워드")
    print(body)

    return dataSendSimple("인기 키워드 순위 입니다\n\n"+res)
