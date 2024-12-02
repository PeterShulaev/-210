s = str(input())
a = s.find('h')
b = s.rfind('h')
c = s[a+1:b]
d = c.replace('h', 'H')
e = s[:a]+'h'+ d + s[b:]
print(e)