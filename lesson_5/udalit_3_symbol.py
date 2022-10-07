s = input()
s_new = ""

for i in range(len(s)):
    if i % 3 != 0:
        s_new = s_new + s[i]
        
print(s_new)