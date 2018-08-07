#!/usr/bin/env python
# coding=utf-8
import sys
class Common():


	@staticmethod
	def readconf(limit=':'):
	    name='conf.txt'
	    file=open(name)
	    dict_arr={}
	    for line in file:
	    	line = line.strip().split(limit);
	    	dict_arr[line[0]]=line[1]
	    return dict_arr
print Common.readconf()
