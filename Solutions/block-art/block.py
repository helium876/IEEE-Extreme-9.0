size = input().split(' ')
size = [int(x) for x in size]
matrix = [0 for i in range(0, size[0] * size[1])] 

nb_op = int(input())

for i in range(0, nb_op):
    op = input().split(' ')
    if op[0] == 'a': 
        for b in range(int(op[1]) - 1, int(op[3])):
            for a in range(int(op[2]) - 1, int(op[4])):
                matrix[b * size[1] + a] += 1
    elif op[0] == 'r':
        for b in range(int(op[1]) - 1, int(op[3])):
            for a in range(int(op[2]) - 1, int(op[4])):
                matrix[b * size[1] + a] -= 1
    elif op[0] == 'q':
        blocks = 0
        for b in range(int(op[1]) - 1, int(op[3])):
            for a in range(int(op[2]) - 1, int(op[4])):
                blocks += matrix[b * size[1] + a]
        print(blocks)

