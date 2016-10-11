a0 = input()
while a0 != "END":
    a1 = str(len(a0)) 
    n = 1
    while str(a1) != a0:
        a0 = a1
        a1 = str(len(a0))
        n += 1
    print(n)
    a0 = input()
