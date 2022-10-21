n = 5

# a = [[0] * n] * n
a = []
for i in range(n):
    b = [0] * n
    a.append(b)

a[2][3] = 99

for i in range(len(a)):
    print(a[i])