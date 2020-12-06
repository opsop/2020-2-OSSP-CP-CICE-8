import sqlite3 as sl
import COVID19Py as covi
import json
from ConstVar import *
import traceback

# db insert query & create global data TABLE
# cols = country(char30) / country_code(char10) / data(json) / LASTUPDATE(DATETIME)
def create_GlobalDB():
    res = covi.COVID19().getAll()
    updateTime = ":".join(res['locations'][0]['last_updated'].split(":")[:-1])
    insertGlData = """INSERT INTO GLOBAL (COUNTRY,COUNTRY_CODE,DATA,LASTUPDATE)
VALUES ('%s','%s','%s', '%s')"""
    #print(json.dumps(res,indent='\t'))
    try:
        # 1. 디비 생성
        conn=sl.connect(DB_PATH+'/corona.db')
        conn.cursor().execute(QCT_global) # 테이블 생성
        before_country=''

        # 2. 디비 데이터 저장 ( 전세계 데이터 따로 저장)
        for i in res['locations']:
            if i['country'] == "Cote d'Ivoire": continue # except nation

            #nested nations sum
            if i['country'] == before_country:
                Q = eval(conn.cursor().execute("Select data from GLOBAL").fetchone()[0])
                for (k,v), (k2,v2) in zip(Q.items(), i['latest'].items()):
                    Q[k] += v2
                conn.execute("""UPDATE GLOBAL SET DATA='%s'
                WHERE COUNTRY='%s' """ %(json.dumps(Q) , before_country))
                continue
            #print(":".join(i['last_updated'].split(":")[:-1]))
            conn.execute(insertGlData %(i['country'],i['country_code'],json.dumps(i['latest']) , updateTime))

            before_country = i['country']

        # data for whole world (국가,국가코드,데이터,최신업데이트시간(초제거))
        conn.execute(insertGlData %('world','전세계',json.dumps(res['latest']) ,updateTime))

    except Exception as e:
      print("ERROR : ", e)
      print(traceback.format_exc())

    finally:
        conn.commit()
        conn.close()

def update_GlobalDB():

    res = covi.COVID19().getAll()
    updateTime = ":".join(res['locations'][0]['last_updated'].split(".")[:-1])
    updateData = "UPDATE GLOBAL SET DATA = '%s', LASTUPDATE = '%s' WHERE COUNTRY = '%s'"
    try:
        # 1. 디비 연결
        conn=sl.connect(DB_PATH+'/corona.db')

        # 2. 디비 업데이트
        for i in res['locations']:
            if i['country'] == "Cote d'Ivoire": continue # except nation

            #nested nations sum
            if i['country'] == before_country:
                # data(json) to dict()
                Q = eval(conn.cursor().execute("Select data from GLOBAL").fetchone()[0])

                #중복국가 데이터 합치기
                for (k,v), (k2,v2) in zip(Q.items(), i['latest'].items()):
                    Q[k] += v2
                conn.execute("""UPDATE GLOBAL SET DATA='%s'
                WHERE COUNTRY='%s' """ %(json.dumps(Q) , before_country))
                continue

            conn.cursor(updateData %(i['latest'],updateTime , i['country']))

            before_country = i['country']

        # 업데이트  data for world (국가,국가코드,데이터,최신업데이트시간(초제거))
        conn.execute( updateData %(res['latest'], updateTime , 'world'))

    except Exception as e:
        print("ERROR : ", e)
        print(traceback.format_exc())
    finally:
        conn.commit()
        conn.close()

#create_GlobalDB()
# 1. db 생성
# 2. db 저장 (미국, 전세계 따로 저장)
# 3. db 업데이트
