a = input().split()
a = [int(num) for num in a]
b = 0
for i in range(1,len(a)-1,1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        b+=1
print(b)
