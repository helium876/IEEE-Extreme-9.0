n = int(input())
m = int(input())
k = int(input())

letters = {}
for i in range(0, k):
    key = input()
    letter = []
    for j in range(0, n):
        letter.append(input())

    letters[key] = letter

factor = int(input())
word = input()

for i in range(0, n):
    line = ""
    for l in word:
        if letters[l][i] == '':
            line += " " * m
        else:
            line += letters[l][i] 

    print(line)
        
