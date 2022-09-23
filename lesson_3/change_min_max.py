a = [int(x) for x in input().split()]

m = min(a)
M = max(a)

m_i = a.index(m)
M_i = a.index(M)

temp = a[m_i]
a[m_i] = a[M_i]
a[M_i] = temp

a = [str(x) for x in a]
answer = " ".join(a)
print(answer)