#!/usr/bin/env python
# coding=utf-8
import MySQLdb
from common import Common

class Db():
	def __init__(self,tableName):

		conf=Common.readconf()
		try:
			host=conf['host']
			part=conf['part']
			user=conf['user']
			pwd =conf['pwd']
			dbname=conf['dbname']
		except:
			print '请配置db'
			exit()
		self.db = MySQLdb.connect(host, user, pwd, dbname, charset='utf8' )
		self.cursor = self.db.cursor()
		self.table = tableName

	def query(self,sql):
		self.cursor.execute(sql)
		results = self.cursor.fetchall()
		return results;
	def insert(self,**arg):
		print arg
		exit()
		str=''
		key=' ('
		value=' ('
		for line in data:
			key=key+line+','
			value=value+','
		key=key[:-1]+') '
		value=value[:-1]+') '
		sql = 'Insert in to '+self.tableName+key+'values'+value;
		print sql
		print self.query(sql);


test=Db('tp_file')
test.query({id:1});

