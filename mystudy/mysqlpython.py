#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:24:29 2018

@author: xutingxi
"""
#python使用mysql
'''
import MySQLdb     python2使用mysqldb这个数据库接口
import pymysql     python3使用mysqldb这个数据库接口
'''
import pymysql
db=pymysql.connect('localhost','root','xtx15275958210','School')
cursor=db.cursor()
version=cursor.execute('select version()')#执行sql查询
data=cursor.fetchone()#获取查询数据
cursor.execute('DROP TABLE IF  EXISTS FIRSTPYTAB')
SQL='''CREATE TABLE FIRSTPYTAB(
        ID INT NOT NULL  PRIMARY KEY AUTO_INCREMENT,
        USERID  float NOT NULL,
        NAME char(10) NOT NULL 
        )'''
cursor.execute(SQL)
a='10aaa'
b=0.238394238
SQLINSERT='''INSERT INTO FIRSTPYTAB(USERID,NAME)
VALUES(0.456,%s),(%s,10.1)'''
cursor.execute(SQLINSERT,[a,b])

a=[10,'dsdd']
SQLINSERT='''INSERT INTO FIRSTPYTAB(USERID,NAME)
VALUES(%s,%s),(245,10.1)'''
cursor.execute(SQLINSERT,a)





db.commit()
SQLSEARCH='''SELECT * FROM FIRSTPYTAB WHERE ID>('%d')'''%2
cursor.execute(SQLSEARCH)
data=cursor.fetchall()

SQLUPDATE='''UPDATE FIRSTPYTAB SET USERID=USERID+1000 WHERE ID>('%d')'''%2
cursor.execute(SQLUPDATE)
db.commit()

SQLDELTTE='''DELETE FROM FIRSTPYTAB WHERE ID=(%d) '''%2
cursor.execute(SQLDELTTE)
db.commit()

SQLNAME='''DESC FIRSTPYTAB '''
SQLNAME='''SHOW COLUMNS FROM FIRSTPYTAB '''
cursor.execute(SQLNAME)
cursor.fetchall()

SQLSORT='''SELECT * FROM FIRSTPYTAB  ORDER BY USERID DESC '''
cursor.execute(SQLSORT)
cursor.fetchall()

SQLGROUP='''SELECT NAME,COUNT(*) FROM FIRSTPYTAB GROUP BY NAME '''
SQLGROUP='''SELECT COALESCE(NAME,'sum'),SUM(ID) AS IID FROM FIRSTPYTAB GROUP BY NAME WITH ROLLUP '''
cursor.execute(SQLGROUP)
cursor.fetchall()

SQLSHOW=''' SHOW TABLES'''
cursor.execute(SQLSHOW)
cursor.fetchall()

SQLALTER=''' ALTER TABLE FIRSTPYTAB ADD SEX CHAR(1)'''#此外还有change 和modify属性
cursor.execute(SQLALTER)
db.commit()

SQLRENAME=''' ALTER TABLE FIRSTPYTAB RENAME TO FIRSTPYTAB1'''
cursor.execute(SQLRENAME)
db.commit()

db.close






