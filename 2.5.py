a = int(input())
b = int(input())
c = int(input())
if a<b:
    if b<c:
        print(a)
    elif b>c:
        if a>c:
            print(c)
        else:
            print(a)
    else:
        print(a)        
elif a>b:
    if b<c:
        print(b)
    elif b>c:
        print(c)
    else:
        print(b)
else:
    if b>c:
        print(c)
    elif c>b:
        print(b)
    else:
        print(a)