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
            try:
		self.cursor.execute(sql)
                self.db.commit()
            except:
                self.db.rollback()
                print 'sql exist error last sql=:'+sql
	def insert(self,data):
		key=' ('
		value=' ('
		for line in data:
			key=key+line+","
			value=value+"'"+str(data[line])+"',"
		key=key[:-1]+') '
		value=value[:-1]+') '
		sql = 'Insert INTO '+self.table+key+'values'+value;
		try:
			self.cursor.execute(sql);
			id=self.db.insert_id()
			self.db.commit()
			return id
		except:
			print 'sql exist error last sql=:'+sql
			exit()
    # def updata(self, data, where):
    #     subsql=''
    #     subwhere=''
    # for line in data:
    #         subsql=subsql+str(line)+'='+str(data[line])+','  
    #     for row in where:
    #         subwhere=subwhere+str(row)+'='+str(where[row])+' and '
    #     subwhere = subwhere[0:-4]
    #     subsql=subsql[0:-1]
    # sql = 'UPDATE '+self.table+' SET '+subsql+' where '+subwhere
    # self.query(sql);

# test=Db('tp_file')
# data={}
# where={}
# data['pid']=1
# data['path_name']=3
# #test.insert(data);
# where['id']=2
# where['path_name']=12
# test.updata(data,where);

