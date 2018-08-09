#!/bin/bash
source ../conf/sh.conf
cat runrecord.txt|while read line
do

        file=`echo $line|awk '{print $1}'`
        num=`echo $line|awk '{print $2}'`
        per=`echo $line|awk '{print $3}'`
        threshold=`echo $line|awk '{print $4}'`
        cmd="sh runmode.sh $tmpdatadir/$file $num $per $threshold"
        echo $cmd
        eval $cmd
        exit 1
done
