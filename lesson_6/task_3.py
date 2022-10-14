n = int(input())
d = {}
for i in range(n):
    a, b = input().split()
    b = int(b)
    old_v = d.get(a, 0)
    d[a] = old_v + b
    
t = d.keys()
t = sorted(t)
for i in range(len(t)):
    w = t[i]
    print(w, d[w])