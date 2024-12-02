s = 0
b = 0
k = 0
z = 0
while True:
    n = int(input())
    if n==0:
        break
    if n>s:
        s=n
        a=0
    if n==s:
        a+=1
print(a)
