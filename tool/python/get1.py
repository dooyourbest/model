import sys
for line in open(sys.argv[1]):
	linearr=line.strip().split(',')
	if linearr[-1]=='1':
		print line.strip()
