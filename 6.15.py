s = 0
a = 0
c = 0 
while True:
    n = int(input())
    if n==0:
        break
    if n!=s:
        a=0
    if n == s:
        a+=1
    if a>c:
        c=a
    s=n
print(c+1)