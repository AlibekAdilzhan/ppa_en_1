n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])

c = 0

for i in range(n - 1):
    is_leader = True
    for j in range(i + 1, n):
        if a[i] < a[j]:
            is_leader = False
    if is_leader == True:
        c = c + 1

print(c)