#!/usr/bin/env python
# coding=utf-8
import os
from analysisFile import AnalysisFile
from common import Common
from sql import Db
import MySQLdb
class File():
	def __init__(self):
		self.allfile=[]
		self.count=0
		conf_dict=Common.readconf()
		if 'path' not in conf_dict:
			path=os.path.realpath(__file__)
			pathRes='/'.join(path.split('/')[:-2])
			conf_dict['path']=pathRes
		self.conf=conf_dict
		self.path=conf_dict['path']
	def getListDir(self,path,level=0,pid=0,codeId=1):
		allfilelist=os.listdir(path);
		allfilelist = filter(self.filterDirAndFile, allfilelist);
		for file in allfilelist:
			filepath=os.path.join(path,file)
			countNum=self.getNum()
			msg=[level,filepath,file,pid]
			if os.path.isdir(filepath):
				msg.append('isdir')
				self.allfile.append(msg)
				subpid=self.addFileMsg(msg,pid)
				sublevel=level+1
				self.getListDir(filepath,sublevel,subpid);
			else:
				msg.append('isfile')
				self.allfile.append(msg)
				filetype=file.split('.')[-1]
				subpid=self.addFileMsg(msg,pid)
				if filetype=='php':
					self.getfileMsg(filepath,subpid)
	def getNum(self):
			self.count=self.count+1
	
			return self.count


	  
	def filterDirAndFile(self, filename):
		filterList=['.DS_Store','.git','.gitignore']
		if filename in filterList:
			 return False
		else:
			 return True
	def addFileMsg(self, msg, pid):
		print msg
		#msg : [level,filepath,file,pid,type][0, '/Users/baidu/doc/.editorconfig', '.editorconfig', 0, 'isfile']
		db=Db('tp_file')
		data={}
		data['level']=msg[0]
		data['path_name']=msg[1]
		data['file_name']=msg[2]
		data['pid']=msg[3]
		data['type']=msg[4]
		if data['type']=='isdir':
			data['type']=0
		else:
			data['type']=1
		resid=db.insert(data);
		return resid

	def addClassMsg(self,msg,pid):
		dbclass=Db('tp_function')
		data={}
		for line in msg:
			data['pid']=str(pid)
			data['function_name']=line['function_name']
			data['params']=line['function_name']
			data['class_extends']=line['extends']
			content = MySQLdb.escape_string(line['comments'])
			data['function_msg']=content
			#data['classname']=line['className']
			# print data;
			# exit()
			res=dbclass.insert(data);


		#exit()
	def getfileMsg(self,path,pid=0):
		any=AnalysisFile(path);
		resList=any.getfileMsg()
		print path;
		if resList:
			self.addClassMsg(resList,pid)
		# print resList
		# print index,className,extendsName;
		# if index ==[] and className =='' and extendsName=='':
		# 	pass
		# else:
		# 	return self.addClassMsg(index,className,extendsName,pid)

		# 	return False



test=File()
test.getListDir(test.path)
test.sortDir(test.allfile)
