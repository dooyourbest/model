#!/bin/bash
cat runrecord.txt|while read line
do

        file=`echo $line|awk '{print $1}'`
        num=`echo $line|awk '{print $2}'`
        per=`echo $line|awk '{print $3}'`
        threshold=`echo $line|awk '{print $4}'`
        sh runmode.sh $file $num $per $threshold
done
