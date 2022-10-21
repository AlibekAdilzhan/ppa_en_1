n = 5

a = [[0] * n for i in range(n)]

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if i == j:
#             a[i][j] = 1

for i in range(len(a)):
    a[i][i] = 1

for i in range(len(a)):
    print(a[i])