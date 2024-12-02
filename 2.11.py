x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x2-x1)<=2 and abs(y1-y2)<=2:
    if abs(x1-x2)==abs(y1-y2):
        print('NO')
    elif x1==x2 or y1==y2: 
        print('NO')
    else:
        print('YES')
else:
    print('NO')
