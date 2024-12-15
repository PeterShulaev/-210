a = input().split()
a = [int(num) for num in a]
b = a[0]
c = 0
for i in range(len(a)):
    if a[i]>b:
        b = a[i]
        c = i
print(b, c)
