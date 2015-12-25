n =int(raw_input())
sady = []
cav = []

for x in xrange(0,n):
	sad = int(raw_input())
	for e in xrange(0,sad):
		s = raw_input().strip().split()
		sady.append(map(int,s))
	cave = int(raw_input())
	for v in xrange(0,cave):
		c = raw_input().strip().split()
		cav.append(map(int,c)) 

