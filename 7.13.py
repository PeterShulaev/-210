a = [int(j) for j in input().split()]
b = 0
for i in range(0,len(a)):
    for s in range(i+1,len(a)):
        if a[i]==a[s]:
            b+=1
print(b)
