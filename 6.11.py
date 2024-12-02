s = 0
b = 0
k = 0
z = 0
while True:
    n = int(input())
    if n==0:
        break
    if n>k:
        k=n
    if n>s:
        k=s
        s=n
print(k)
