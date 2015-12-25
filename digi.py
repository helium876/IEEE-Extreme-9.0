def func(x):
	y = str(x)
	count = len(y)
	if count == x:
		return 1
	else:
		x = count
		return 1 + func(x)

c = 0
ans =[]
while True:
	inp = raw_input()
	if inp == "END":
		break
	tt = int(inp)
	i = func(tt)
	ans.append(i)
	c = c + 1

loop = len(ans)
for x in xrange(0,loop):
	print ans[x]