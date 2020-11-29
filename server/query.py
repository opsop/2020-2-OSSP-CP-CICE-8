import sqlite3 as sl
import COVID19Py as covi
import json
from variable import *

# db insert query & create global data TABLE
# cols = country(char30) / country_code(char10) / data(json)
def insert_db():
    res = covi.COVID19().getAll()
    #print(json.dumps(res,indent='\t'))
    db(post)
    conn=sl.connect(DB_PATH+'/corona.db')
    res = res['locations']
    before_country=''

    for i in res:
        if i['country'] == "Cote d'Ivoire": continue # except nation

        #nested nations sum
        if i['country'] == before_country:
            Q = eval(conn.cursor().execute("Select data from GLOBAL").fetchone()[0])
            for (k,v), (k2,v2) in zip(Q.items(), i['latest'].items()):
                Q[k] += v2
            conn.execute("""UPDATE GLOBAL SET DATA='%s'
            WHERE COUNTRY='%s' """ %(json.dumps(Q) , before_country))
            continue


        conn.execute("""INSERT INTO GLOBAL (COUNTRY,COUNTRY_CODE,DATA)
  VALUES ('%s','%s','%s')""" %(i['country'],i['country_code'],json.dumps(i['latest'])))

        before_country = i['country']


    conn.commit()
    conn.close()

# create db table
def db(data):
    conn=sl.connect(DB_PATH+'/corona.db')
    conn.execute(QCT_global)
    data = data['action']['detailParams']
    situation = ['confirmed','deaths','recovered']

    if data['sys_nation']['value'] == '전세계':
        if data['situation']['value'] == 'situation':
            res = covi.COVID19().getLatest()
            print(res)
            conn.execute("""INSERT INTO GLOBAL (COUNTRY,country_code,data)
          VALUES ( '%s' ,'%s', '%s' )""" %('world','전세계',json.dumps(res)))

    #cursor = conn.cursor().execute("SELECT * from GLOBAL")
    #[print(i[0] ,'\t',end='') for i in cursor.description]
    #print(cursor.fetchall())
    conn.commit()
    conn.close()
#insert_db()
#[print("'%s' : '%s' , "%(i1 ,i2)) for i1,i2 in conn.cursor().execute("SELECT country,country_code from global").fetchall()]
