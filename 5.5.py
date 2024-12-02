s = str(input())
b = s.find('f')
c = s.rfind('f')
if b==c==-1:
    print('')
elif b == c:
    print(b)
else:
    print(b, c)
