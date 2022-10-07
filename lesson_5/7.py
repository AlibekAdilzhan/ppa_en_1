n = int(input())
a = input().split()
k = int(input())

b = [0] * n # b = [0, 0, 0, 0, 0, 0]

for i in range(n):
    b[(i + k) % n] = a[i]

print(a)
print(b)