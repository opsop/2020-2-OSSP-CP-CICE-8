# KoreaDB 정의 및 사용 함수들 정의된 파일
import sqlite3 

# https://somjang.tistory.com/entry/Python-Python에서-Sqlite3-사용하기 [솜씨좋은장씨]
# https://wings2pc.tistory.com/entry/웹-앱프로그래밍-파이썬-플라스크Python-Flask-Request-데이터-DB-저장SQLite3-사용 [Wings on PC]

def create_table(): 
    try: 
        db = sqlite3.connect("KoreaDB.db") 
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
    db = sqlite3.connect("KoreaDB.db") 
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
def insert_data(updateTime, TotalCase, TotalDeath, TotalRecovered, NowCase, TotalChecking, TodayCase, TodayRecovered): 
    try: 
        db = sqlite3.connect("KoreaDB.db") 
        c = db.cursor() 
        setdata = (updateTime, TotalCase, TotalDeath, TotalRecovered, NowCase, TotalChecking, TodayCase, TodayRecovered) 
        c.execute("INSERT INTO KoreaDB VALUES (?, ?, ?, ?, ?, ?, ?, ?)", setdata) 
        db.commit() 
    except Exception as e: 
        print('db error: here', e) 
    finally: 
        db.close()


def select_all(): 
    ret = list() 
    try: 
        db = sqlite3.connect("KoreaDB.db") 
        c = db.cursor() 
        c.execute('SELECT * FROM KoreaDB') 
        ret = c.fetchall() 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close() 
        return ret


def select_updataTime(updateTime): 
    ret = () 
    try: 
        db = sqlite3.connect("KoreaDB.db")
        c = db.cursor() 
        setdata = (updateTime,) 
        c.execute('SELECT * FROM KoreaDB WHERE updateTime = ?', setdata) 
        ret = c.fetchone() 
    except Exception as e: 
            print('db error:', e) 
    finally: 
            db.close() 
            return ret


