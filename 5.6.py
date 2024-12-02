s = str(input())
g = s.count('f')
if g==1:
    print('-1')
elif g==0:
    print('-2')
elif g>0:
    a = s.find('f')
    b = s.find('f',a+1)
    print(b)
