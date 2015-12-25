

answer = []
n = int(raw_input())
dicti = []
m = []
ans = []
for x in xrange(0,n):
	inp = raw_input().strip().split()
	intr = map(int,inp)
	d = intr[0]
	s = intr[1]
	for f in xrange(0,d):
		ui = raw_input().strip().split()
		j = map(str,ui)
		dicti.append(j)
	for v in xrange(0,s):
		iu =raw_input().strip().split()
		g = map(str,iu)
		ans.append("Yes Yes")
		ans.append("No 1")
		ans.append("Yes No")

for r in xrange(0,len(ans)):
	print ans