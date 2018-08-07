#!/bin/bash
python getmsg.py $1 $2 $3>tmp.txt
python model-training-logistic-regression.py tmp.txt $4
sh insetdb.sh logistic-regression.model $1 $2 $3 $4