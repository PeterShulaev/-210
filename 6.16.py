import math
total_sum = 0
a = 0
n = []
while True:
    x = int(input())
        
    if x == 0:
        break
    n.append(x)
    total_sum+=x
    a+=1
mean= total_sum/a #среднее арифметическое
suum2=sum((x-mean)**2 for x in n)
itog=math.sqrt(suum2/(a-1))
print(itog)
