#base = "http://www.ieee.com"
#target = "http://www.ieee.org"


base = input()
h = [hex(ord(x)) for x in base]
hexbase = [int(hex(ord(x)), 0) for x in base]

n = int(input())

for i in range(0, 1):
    url = input()
    cpybase = base
    while len(cpybase) < len(url):
        cpybase += base
    cpybase = cpybase[:len(url)]
   
    chose = [hex(ord(x)) for x in url] 
    machin = [hex(ord(x)) for x in cpybase]

    xored = [hex(int(x) ^ int(y)) for (x, y) in zip(chose, machin)]
   
    print(xored)
    
    #hexurl = [int(hex(ord(x)), 0) for x in url]


    #xorlol = [hex(a ^ b) for (a, b) in zip(hexbase, hexurl)]




