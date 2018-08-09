#!/usr/bin/env python
# coding=utf-8
import sys
import os
class Common():


	@staticmethod
	def readconf(limit=':'):
	    name='../conf/py.conf'
	    file=open(name)
	    dict_arr={}
	    for line in file:
	    	line = line.strip().split(limit);
	    	dict_arr[line[0]]=line[1]
	    return dict_arr
	@staticmethod
	def getDir(self):
		return os.getcwd()
	@staticmethod
	def getRoot(self):
		return os.getcwd()+'/../'
	@staticmethod
	def getModel(self):
		return os.getcwd()+'/../dealModel'
	@staticmethod
	def getMindResDir(self):
		return os.getcwd()+'/../mindRes'


print Common.readconf()
