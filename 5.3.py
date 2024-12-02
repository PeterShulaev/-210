s = input()
b = len(s)
c = b // 2
if b % 2 != 0:
    c += 1
g = s[c:] + s[:c]
print(g)
