t = int(input())
for i in range(0, t):
    arr = input().split(' ')
    arr = [int(x) for x in arr]

    switches = {}
    for j in range(1, arr[0] + 1):
        switches[j] = "Off"

    for j in range(2, len(arr)):
        for k in range(arr[j], arr[0] + 1, arr[j]):
            if switches[k] == "Off":
                switches[k] = "On"
            elif switches[k] == "On":
                switches[k] = "Off"

    i = 0
    for e in switches.keys():
        if switches[e] == "On":
            i += 1

    print(i)
