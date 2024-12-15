a = input().split()
a = [int(num) for num in a]
rost = int(input())
p = 1
for i in range(len(a)):
    if rost <=a[i]:
        p+=1
print(p)
