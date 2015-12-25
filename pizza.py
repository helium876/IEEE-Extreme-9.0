ans =[]
while True:
	try:
		inp = raw_input()
		divs = int(inp)/2
		n = divs +3
		ans.append(n)
	except EOFError:
		break
	

loop =len(ans)
for x in xrange(0,loop):
	print ans[x]