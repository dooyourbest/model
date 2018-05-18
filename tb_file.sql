CREATE TABLE `tp_file` (
  `id` bigint(12) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `file_name` varchar(128) NOT NULL DEFAULT '0' COMMENT '文件名',
  `pid` bigint(21) NOT NULL COMMENT '上级id',
  `path_name` varchar(128) NOT NULL COMMENT '路径名',
  `file_msg` varchar(128) NOT NULL COMMENT '文件信息',
  `class_name` varchar(128) NOT NULL COMMENT '类名',
  `class_msg` varchar(128) NOT NULL DEFAULT '0' COMMENT '类信息',
  `detail` varchar(128) NOT NULL COMMENT '额外信息',
  `codeId` int(11) unsigned NOT NULL COMMENT '代码库id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='文件表'

