a = int(input())
b = int(input())
c = int(input())
d = int((a+b+c)/2)
if a%2==b%2==c%2==0:
    print(d)
elif a%2==b%2==c%2==1:
    print(d+2)
else:
    print(d+1)
