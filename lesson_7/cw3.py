A = [
    [1, 2, 3, 0],
    [-1, 0, 1, 1],
    [0, 8, 9, 1],
    [1, 1, 1, 0]
]

s = 0

for i in range(len(A)):
    s = 0
    for j in range(len(A[i])):
        s = s + A[i][j]
    print(s, end=" ")