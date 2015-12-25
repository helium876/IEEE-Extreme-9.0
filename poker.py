def func(p1,p2,p3):
	while p1 > 0 and p2 > 0 and p3 > 0:
	word = str(p1)+" "+str(p2)+" "+str(p3)
	string.append(word)
	if p1 > p2 and p1 > p3:
		if p2 < p3:
			p1 = p1 - p2
			p2 = p2 * 2
			if p3 < p1:
				p1 = p1 - p3
				p3 = p3 * 2
		else:
			p1 = p1 - p3
			p3 = p3 * 2
			if p2 < p1:
				p1 = p1 - p2
				p2 = p2 * 2
	elif p2 > p1 or p2 > p3:
		if p1 < p3:
			p2 = p2 - p1
			p1 = p1 * 2
			if p3 < p2:
				p2 = p2 -p3
				p3 = p3 * 2
		else:
			p2 = p2 - p3
			p3 = p3 * 2
			if p1 < p3:
				p2 = p2 - p1
				p1 = p1 * 2
	else:
		if p1 < p2:
			p3 = p3 - p1
			p1 = p1 * 2
			if p2 < p3:
				p3 = p3 - p2
				p2 = p2 * 2
		else:
			p3 = p3 - p2
			p2 = p2 * 2
			if p1 < p3:
				p3 = p3 - p1
				p1 = p1 * 2
	count  =count + 1
	if count >= 15:
		string = ["Ok"]
		break
inp = raw_input().strip().split()
intr = map(int,inp)
p1 = intr[0]
p2 = intr[1]
p3 = intr[2]
string = []
count =0


loop = len(string)
for x in xrange(0,loop):
	print string[x]
