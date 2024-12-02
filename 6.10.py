a= 0
s=0
while True:
    n = int(input())
    if n==0:
        break
    if n>s:
        a+=1
    s=n
print(a)