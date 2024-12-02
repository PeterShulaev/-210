n = int(input())
x = 0
y = 1
z = x+y
a = 0
if n==0:
    z =0
if n==1:
    z=1
while n-1>0:
    n-=1
    if a ==0:
        a+=1
        continue
    x = y 
    y = z
    z = x+y
print(z)