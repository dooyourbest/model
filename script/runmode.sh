#!/bin/bash
source ../conf/sh.conf
cmd="python $pytooldir/getmsg.py $1 $2 $3 > tmp.txt"
echo $cmd
eval $cmd
python $dealmodeldir/mind.py tmp.txt $4
sh insetdb.sh $mindresdir/logistic-regression.model $1 $2 $3 $4