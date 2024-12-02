s = str(input())
a = s.find('h')
b = s.rfind('h')
c = s[:a] + s[b:a:-1] + s[b:]
print(c)