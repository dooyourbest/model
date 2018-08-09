import sys
for line in open(sys.argv[1]):
	if line.strip()[-1]=='0':
		print line.strip()
