import sys
for line in open(sys.argv[1]):
         print '1,'+','.join(line.strip().split(',')[1:])
