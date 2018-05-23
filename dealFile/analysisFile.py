#!/usr/bin/env python
# coding=utf-8
import re
class AnalysisFile():
    def __init__(self, filePath):
        self.limitConf={}
        self.limitConf['lineComment']='^\s*//'
        self.limitConf['blockStart'] = '^\s*/\*+'
        self.limitConf['blockEnd'] = '^\s*\*/'
        self.limitConf['function'] = '^\s*(public|private|protect|\s*)\s*function\s+'
        self.limitConf['class'] = '^\s*class\s+.*'
        self.limitConf['extends'] ='\s+extends\s+'
        self.className=''
        self.extendsName=''
        self.file = open(filePath);
        self.search=['function','']
        self.text={}
        self.textStruct={}
        self.codeStruct=[]
        self.fileAllLine=0
        self.singleComments={}
        self.fileList = []  
        self.filePath=filePath 
        self.readFile()
        self.index=[]
    def readFile(self):
        """遍历文件 ，针对每一行做处理"""
        lineNum=1;
        self.fileList.append('first')
        for line in self.file:
            self.fileList.append(line.strip(''))
            self.analysis(line, lineNum);
            lineNum = lineNum+1
            self.fileAllLine=lineNum
        if 'class' in self.text:
            self.getCLassName(self.text['class'][0])
            del self.text['class']
        if 'extends' in self.text:
            self.getExtends(self.text['extends'][0])
            del self.text['extends'];
    def analysis(self, line, lineNum):
        limitConf = self.limitConf
        for config in limitConf: 	
        	res = re.search(limitConf[config], line)
        	if not res:
                    pass
        	else:
                    #print line
               	    if config in self.text:
        	        self.text[config].append(lineNum)

        	    else:
        	        self.text[config]=[lineNum]
    def analysisFileStruct(self):
        self.textStruct={}
        allTextMsg=self.text
        for dictConfMsg in allTextMsg:
            for row in allTextMsg[dictConfMsg]:
                self.textStruct[int(row)]=dictConfMsg

    def organizaStruct(self):
        for line in range(1,self.fileAllLine+1):
            try:
                self.textStruct[line]
            except:
                pass
    def organizaCodeStruct(self):
        textStruct=self.textStruct
        for line in range(1,self.fileAllLine):
            try:
                if textStruct[line]!='blockStart' and textStruct[line]!='blockEnd':
                    msg={}
                    msg['name']=textStruct[line];
                    msg['lineNum']=line
                    self.codeStruct.append(msg)
                else:
                    self.getComments(line,textStruct[line])
            except:
                pass
        # print self.filePath
        # for line in self.codeStruct:
            # print line
                
    def getComments(self, line, type):
        if type == 'blockStart':
            if 'start' in self.singleComments:
                pass
            else:
                self.singleComments['start']=line
        else:
            try:
                self.singleComments['end']=line
                lineNum=str(self.singleComments['start'])+':'+str(self.singleComments['end'])
                msg={'name':'CommentsBlock','lineNum':lineNum}
                self.codeStruct.append(msg)
                self.singleComments={}
            except:
                print self.singleComments
                print 'error'
                exit(123)

    def createIndex(self):
        for i in range(len(self.codeStruct)):
            type = self.codeStruct[i]['name']
            lineNum = self.codeStruct[i]['lineNum']
            functionMsg = {}
            if type=='function':
                functionMsg['function']= self.getFunction(lineNum)
                if self.codeStruct[i-1]['name']=='CommentsBlock' and i>=1:  # 注意list[0-1]=list[-1]
                    comments=self.codeStruct[i-1]['lineNum'].split(':')
                    if int(lineNum)-int(comments[1])<2:
                        commentsList=[]
                        for i in range(int(comments[0]), int(comments[1])+1):
                            commentsList.append(self.fileList[i].strip())
                            functionMsg['comments'] =';'.join(commentsList)
                    else:
                        functionMsg['comments']=''
                else:
                    functionMsg['comments'] =''
                # try:
                #     print functionMsg['comments']
                # except:
                #     print self.filePath
                #     print self.codeStruct[i]['lineNum'];
                self.index.append(functionMsg);

    def getCLassName(self,lineNumber):
        line = self.fileList[lineNumber]
        res = re.search('class\s+\w+\s*',line)
        try:
            self.className=res.group()[5:].strip()
        except:
            print 'error:'
            print self.filePath
            print 'lineNumber:'+str(lineNumber)
            print 'get Class error'
            exit()
    def getExtends(self,lineNumber):
        line = self.fileList[lineNumber]
        res = re.search('\s{1}extends\s+\w+\s*',line)
        try:
            self.extendsName = res.group().strip()[7:].strip()
        except:
            print 'error:'
            print self.filePath
            print 'lineNumber:'+str(lineNumber)
            print 'get Extends error'
            exit()

    def getFunction(self, lineNumber):
        functionDict={}
        line =self.fileList[lineNumber]
        res = re.search('function\s+.+\(',line)
        try:
            functionName = res.group().strip()[8:-1].strip()
            functionDict['name'] = functionName
        except:
            print 'error:'
            print self.filePath
            print 'lineNumber:'+str(lineNumber)
            print 'get Function error'
            exit()
        res=re.search('\(.*\)',line)
        try:
            funcStr = res.group()
            params=','.join(funcStr[1:-1].split(','))
            functionDict['params']=params
        except:
            functionDict['params']=''
        return functionDict
    def getfileMsg(self):
        self.analysisFileStruct()
        self.organizaCodeStruct()
        self.createIndex() 
        list=[]
        if self.className=='' and self.extendsName=='' and self.index==[]:
            return False
        if self.index:
            for line in self.index:
                try:
                    msg={}
                    msg['className']=self.className
                    msg['extends']=self.extendsName
                    msg['function_name']=line['function']['name']
                    msg['params']=line['function']['params']
                    # msg['comments']=line['comments']
                    msg['comments']=''
                except:
                    print line
                    exit()
                list.append(msg)
        else:
            msg={}
            msg['params']=''
            msg['className']=self.className
            msg['extends']=self.extendsName
            msg['function_name']=''
            msg['comments']=''
            list.append(msg)
        return list

# any=AnalysisFile('../test.php')
# any.getfileMsg()


