n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
k = int(input())

c = 0

for i in range(n - 2):
    if k == a[i] + a[i + 1] + a[i + 2]:
        c = c + 1

print(c)