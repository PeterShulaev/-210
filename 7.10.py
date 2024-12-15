a = input().split()
a = [int(num) for num in a]
max = a[0]
c = 0
min = a[0]
d = 0
for i in range(len(a)):
    if a[i]>max:
        max = a[i]
        c = i
for s in range(len(a)):
    if a[s]<min:
        min = a[s]
        d = s
a[c],a[d]=a[d],a[c]
b = ' '.join(str(x) for x in a)
print(b)
