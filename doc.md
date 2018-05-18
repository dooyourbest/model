本项目用于生成文档，目前阶段目标
1生成基于目录结构的类的信息如下
 ---aaa
 -----php文件
 --------class name
 --------class function
 --------class extend 等信息
 -----b目录
-----php文件
 --------class name
 --------class function
 --------class extend 等信息
拟采用python遍历文件正则抓取数据，形成目录结构，存入数据库中，然后进行处理
目前想法
对于单个文件
	1 使用python 正则清除相关的注释 包括两种
	 1）块注释 /** 开始*/结尾  
	 2）行注释 //开始 一行都是注释
	2 清理完注释，然后用正则匹配关键字（class ,function ,extends）
	3 形成数据库
	对于function 之前/**/注释的文件，我们考虑是否进行读取?如何读取

形成并组织数据库
我们的目的是形成文档，所以我们需要规划展现形式来构建数据库

我们目前展现形式要求
1首先我们能够补充文档，增加注释  
  首先针对函数应用
    1首先要function  函数名称 适合模糊搜索
    				路径     目录展示
    				参数注释  json比较合适存储
    				函数注释  字符串
    				代码（要能更新）//todo


    2同时也能够完整的读取文档，甚至是直接观察方法源码
                    函数名称搜索
                    函数路径展示
                    函数参数展示
                    函数作用

2树状结构
   path 层 path路径递归展示//类名亦可以标识，选用文件比较适合
   class 代码结构展示依赖 class依赖
   function 重写继承展示//todo 依赖于分析

3 类展示
   类的结构展示，包含的function 等信息

附加信息，以上是针对comlib
    
    api文档组织，接口外露，参数等信息
 	之后可以增加构建工具，先写文档，然后生成代码 //todo


数据库组织
  细粒度划分
  1 类（文件、文件夹），
  
  2 函数（单个类的信息）


首先我们划分为两个表，1 文件/类 2 函数，
tb_file
tb_fucntion
根据上述组织结构
file 主要是文件层次的划分，其实也是树状结构的划分。字段组织
1 id 毋庸置疑
2 filename 文件名/目录明
3 type 类型 文件/目录 记录型信息
4 pid 父级id 依赖
5 pathname 依赖于文件名的pathname组织 =pid的pathname+'/'+filename
6 fileMsg 文件/目录的的一些介绍信息
6 classname 如果是class文件，class的名称
7 classmsg class文件的文件信息
8 detail 额外x信息
9  codeId 代码库id



tb_function 
1 id 毋庸置疑
2 pid 依赖的文件，关联tb_file（可以根据文件找到类级别的一系列信息）
3 functionName 函数名称
4 params 函数参数和相对应的注释 json比较合适
5 functionMsg 函数作用
6 functionCode //todo
7 function 
8 classExtends 类的关联类名称//依赖后续分析
9 detail 额外信息
10 CodeId



代码升级之后，代码库也要有标识
tb_code
id
codeName
codeMsg










