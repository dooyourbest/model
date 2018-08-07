#!/usr/bin/env python
# coding=utf-8
from common import Common
import MySQLdb
#获取配置信息

conf = Common.readconf()
host=conf['host']
user=conf['user']
passwd=conf['pwd']
dbname=conf['dbname']
#连接数据库
conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='')

cursor=conn.cursor()

try:
      cursor.execute("create database if not exists "+dbname)
except:
      pass
conn.select_db(dbname)

try:
      cursor.execute("drop table model")
except:
      pass
tableConf=['../model.sql']
for line in tableConf:
      sqlCreateTable=open(line).read()
      cursor.execute(sqlCreateTable)
cursor.close()
 
