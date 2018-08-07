#!/bin/bash
file=$1
filename="'$file'"
if [[ -z $filename ]]
then
	echo input----file,type,num,zhengpersent,note
	exit 12
fi
type="'$2'"
num="'$3'"
zhengpersent=$4
threshold=$5
note="'$6'"
if [[ -z $note ]]
then
note="''"
fi
negprecision=`grep neg $file|awk '{print $2}'`
negrecall=`grep neg $file|awk '{print $3}'`
negf1score=`grep neg $file|awk '{print $4}'`
negpsupport=`grep neg $file|awk '{print $5}'`
posprecision=`grep pos $file|awk '{print $2}'`
posrecall=`grep pos $file|awk '{print $3}'`
posf1score=`grep pos $file|awk '{print $4}'`
pospsupport=`grep pos $file|awk '{print $5}'`
allprecision=`grep total $file|awk '{print $4}'`
allrecall=`grep total $file|awk '{print $5}'`
allf1score=`grep total $file|awk '{print $6}'`
allpsupport=`grep total $file|awk '{print $7}'`
accuracy=`grep 模型准确率 $file|awk '{print $2}'`
auc=`grep AUC $file|awk '{print $2}'`
echo "use model;INSERT INTO model (threshold,accuracy,filename,type,num,zhengpersent,note,negprecision,negrecall,negf1score,negpsupport,posprecision,posrecall,posf1score,pospsupport,allprecision,allrecall,allf1score ,allpsupport,auc) values ($threshold,$accuracy,$filename,$type,$num,$zhengpersent,$note,$negprecision,$negrecall,$negf1score,$negpsupport,$posprecision,$posrecall,$posf1score,$pospsupport,$allprecision,$allrecall,$allf1score ,$allpsupport,$auc);"|mysql -h 10.99.110.223 -P3306 -uroot