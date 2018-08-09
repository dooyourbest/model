import sys
allnum=sys.argv[2]
persent10=sys.argv[3]
trueSample=[];
falseSample=[];
for line in open(sys.argv[1]):
    if line.strip()[-1]=='1':
        trueSample.append(line.strip())
    else:
        falseSample.append(line.strip())
allnum=int(allnum)
truenum = int(int(allnum)*float(persent10))
falsenum = allnum - truenum
def fillsample(sample,number):
    real = len(sample)
    for index in range(0,number):
        if real<number:
            index = index % real
        print sample[index]

fillsample(trueSample,truenum)
fillsample(falseSample,falsenum)
