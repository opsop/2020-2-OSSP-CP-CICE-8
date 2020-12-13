# KoreaDB 정의 및 사용 함수들 정의된 파일
import sqlite3
import os

KoreaDBPath = os.path.dirname(__file__) + '/CoronaBotDB/KoreaDB.db'
# KoreaDBPath="KoreaDB.db"
# https://somjang.tistory.com/entry/Python-Python에서-Sqlite3-사용하기 [솜씨좋은장씨]
# https://wings2pc.tistory.com/entry/웹-앱프로그래밍-파이썬-플라스크Python-Flask-Request-데이터-DB-저장SQLite3-사용 [Wings on PC]

# DB 테이블 새로 생성
def create_table():
    try:
        db = sqlite3.connect(KoreaDBPath)
        c = db.cursor()
        c.execute('CREATE TABLE KoreaDB(updateTime TEXT PRIMARY KEY, TotalCase TEXT, TotalDeath TEXT, TotalRecovered TEXT, NowCase TEXT, TotalChecking TEXT, TodayCase TEXT, TodayRecovered TEXT)')
        c.executemany(
        'INSERT INTO KoreaDB VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
        [('2020.11.23', '31,004', '509', '26,539', '3,956', '2,922,135', '271', '73'),
        ('2020.11.24', '31,353', '510', '26,722', '4,121', '2,946,399', '349', '183'),
        ('2020.11.25', '31,735', '513', '26,825', '4,397', '2,966,405', '382', '103'),
        ('2020.11.26', '32,318', '515', '26,950', '4,853', '2,988,046', '583', '125'),
        ('2020.11.27', '32,887', '516', '27,103', '5,268', '3,009,577', '569', '153')] )
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

'''
try:
    db = sqlite3.connect(KoreaDBPath + '/KoreaDB.db')
    c = db.cursor()
    c.execute('CREATE TABLE KoreaDB(updateTime TEXT PRIMARY KEY, TotalCase TEXT, TotalDeath TEXT, TotalRecovered TEXT, NowCase TEXT, TotalChecking TEXT, TodayCase TEXT, TodayRecovered TEXT)')
    c.executemany(
    'INSERT INTO KoreaDB VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
    [('2020.11.23', '31,004', '509', '26,539', '3,956', '2,922,135', '271', '73'),
    ('2020.11.24', '31,353', '510', '26,722', '4,121', '2,946,399', '349', '183'),
    ('2020.11.25', '31,735', '513', '26,825', '4,397', '2,966,405', '382', '103'),
    ('2020.11.26', '32,318', '515', '26,950', '4,853', '2,988,046', '583', '125'),
    ('2020.11.27', '32,887', '516', '27,103', '5,268', '3,009,577', '569', '153')] )
    db.commit()
    db.close()
except Exception as e:
    print('db error:', e)
finally:
    db.close()
'''

# 데이터 삽입
def insert_data(updateTime, TotalCase, TotalDeath, TotalRecovered, NowCase, TotalChecking, TodayCase, TodayRecovered):
    # updateTime/ TotalCase/ TotalDeath/ TotalRecovered/ NowCase/ TotalChecking/ TodayCase/ TodayRecovered
    # 업데이트 날짜/ 총 확진자/ 총 사망자/ 총 완치자/ 격리자 수/ 총 검사완료자/ 어제 대비 확진자/ 어제대비 완치자
    try:
        db = sqlite3.connect(KoreaDBPath)
        c = db.cursor()
        setdata = (updateTime, TotalCase, TotalDeath, TotalRecovered, NowCase, TotalChecking, TodayCase, TodayRecovered)
        c.execute("INSERT INTO KoreaDB VALUES (?, ?, ?, ?, ?, ?, ?, ?)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()


# 전체 데이터 가져오기
def select_all():
    ret = list()
    try:
        db = sqlite3.connect(KoreaDBPath)
        c = db.cursor()
        c.execute('SELECT * FROM KoreaDB')
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret


# 특정 updateTime의 row 값 가져오기
def select_updateTime(updateTime):
    ret = ()
    try:
        db = sqlite3.connect(KoreaDBPath)
        c = db.cursor()
        setdata = (updateTime,)
        c.execute('SELECT * FROM KoreaDB WHERE updateTime = ?', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e,"\n")
    finally:
        db.close()
        print(type(ret))
        return ret


# 특정 updateTime의 row 값 삭제하기
def delete_updateTime(updateTime):
    # ret = ()
    try:
        db = sqlite3.connect(KoreaDBPath)
        c = db.cursor()
        setdata = (updateTime,)
        c.execute("DELETE FROM KoreaDB WHERE updateTime = ?", setdata)
        
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return
