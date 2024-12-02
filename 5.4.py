s = str(input())
a = s.find(' ') + 1
g = s[a:]+' '+s[:a]
print(g)