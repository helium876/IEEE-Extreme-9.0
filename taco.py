d = int(raw_input())
if d <= 1000:
	amt_taco =[]
	for x in xrange(0,d):
		inp =raw_input().strip().split()
		ingr = map(int,inp)
		s = ingr[0]
		m = ingr[1]
		r = ingr[2]
		b = ingr[3]
		total_i = m + r + b
		amt = total_i/2
		if amt > s:
			amt_taco.append(s)
		else:
			amt_taco.append(amt)

loop = len(amt_taco)
for x in xrange(0,loop):
	print amt_taco[x]