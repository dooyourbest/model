#!/usr/bin/env python
# coding=utf-8
import sys
import os
class File():
	def __init__(self):
		fileconf=open('conf.txt');
		self.allfile=[]
		self.count=0
		conf_dict={}
		for line in fileconf:
			line = line.strip().split(':');
			conf_dict[line[0]]=line[1];
		if not conf_dict['path']:
			print '请配置conf.txt文件中的path目录'
			exit(1)
		else:
			self.conf=conf_dict
			self.path=conf_dict['path']
	# def listFile(self):
	# 	for dirpath,dirnames,filenames in os.walk(self.path):


	# 		print dirpath
	# 		print dirnames
	# 		print filenames
	def getListDir(self,path,level=0,pid=0):
		allfilelist=os.listdir(path);
		for file in allfilelist:

			filepath=os.path.join(path,file)
			countNum=self.getNum()

			if os.path.isdir(filepath):
				self.allfile.append([level,filepath,file,'isdir',countNum])
				sublevel=level+1
				self.getListDir(filepath,sublevel);
			else:
				self.allfile.append([level,filepath,'isfile',countNum])
				# self.allfile.append(filepath);
	def sortDir(self,sortDir):
		dir={}
		for line in sortDir:
			print line
			# level = sortDir[line][0]
			# if level in dir:
			# 	dir[level].append([line,sortDir[line][1]])
			# else:
			# 	dir[level]=[[line,sortDir[line][1]]]
	def getNum(self):
		 self.count=self.count+1
		 return self.count


	 # def listDir(self,path):
	 # 	allfilelist=os.listdir(path);




test=file()
test.getListDir(test.path)
test.sortDir(test.allfile)