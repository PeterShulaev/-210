A = int(input())
x = 0
a=0
y = 1
z = x+y
n=100
m  = 2 
if A==0:
    z =0
    print(z)
if A==1:
    z=0
    print(z)
while n>0:
    n-=1
    m+=1
    x = y 
    y = z
    z = x+y
    if A==z:
        a+=1
        print(m)
        break 
    if z!=A:
        continue
if a==0:
    print(-1)