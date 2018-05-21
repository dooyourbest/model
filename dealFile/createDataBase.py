#!/usr/bin/env python
# coding=utf-8
import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='')
cursor=conn.cursor()
cursor.execute("""create database if not exists doc""")
conn.select_db('doc')
cursor.execute("CREATE TABLE `tp_file` ( \
      `id` bigint(12) NOT NULL AUTO_INCREMENT COMMENT 'ID',\
      `file_name` varchar(128) NOT NULL DEFAULT '0' COMMENT '文件名',\
      `pid` bigint(21) NOT NULL COMMENT '上级id',\
      `path_name` varchar(128) NOT NULL COMMENT '路径名',\
      `file_msg` varchar(128) NOT NULL COMMENT '文件信息',\
      `class_name` varchar(128) NOT NULL COMMENT '类名',\
      `class_msg` varchar(128) NOT NULL DEFAULT '0' COMMENT '类信息',\
      `detail` varchar(128) NOT NULL COMMENT '额外信息',\
      `codeId` int(11) unsigned NOT NULL COMMENT '代码库id',\
      PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='文件表'")
cursor.execute("CREATE TABLE `tp_function` ( \
      `id` bigint(12) NOT NULL AUTO_INCREMENT COMMENT 'ID',\
      `pid` bigint(21) NOT NULL COMMENT '依赖的文件，关联tb_file（可以根据文件找到类级别的一系列信息',\
      `function_name` varchar(128) NOT NULL COMMENT '函数名称',\
      `params` varchar(128) NOT NULL COMMENT '函数参数和相对应的注释 json比较合适',\
      `function_msg` varchar(128) NOT NULL COMMENT 'functionMsg',\
      `function_code` varchar(128) NOT NULL DEFAULT ' ' COMMENT 'code',\
      `function_note` varchar(128) NOT NULL COMMENT '函数额外信息',\
      `class_extends` varchar(128) NOT NULL COMMENT '类的关联类名称',\
      `detail` varchar(128) NOT NULL COMMENT '额外信息',\
      `codeId` int(11) unsigned NOT NULL COMMENT '代码库id',\
      PRIMARY KEY (`id`)\
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='文件表'")
cursor.close()
 
