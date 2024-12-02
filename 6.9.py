s = 0
b = 0
k = 0
while True:
    n = int(input())
    if n==0:
        break
    if n>s:
        s=n
        k=b
    b+=1
print(k)
