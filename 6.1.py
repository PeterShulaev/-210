N = int(input())
a=1
z=0
while a <=N:
    if z==0:
        print(a,end=' ')
        z+=1
    for i in range(1,a):
        if(i*i==a):
            print(a,end=' ')
    a+=1
print()