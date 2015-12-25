size = int(input())
for i in range(0, size):
    arr = input().split(' ')
    arr = [int(x) for x in arr]
    tacos = 0
    shells = arr[0]
    for i in range(0, shells):
        if arr[1] != 0 and arr[2] != 0:
            arr[1] -= 1
            arr[2] -= 1
            arr[0] -= 1
            tacos += 1
        elif arr[3] != 0 and arr[2] != 0:
            arr[3] -= 1
            arr[2] -= 1
            arr[0] -= 1
            tacos += 1
        else:
            break

        print(arr)

    print(tacos)
