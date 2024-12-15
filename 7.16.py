x = []
y = []
for i in range(8):

 x1, y1 = [int(s) for s in input().split()]
 x.append(x1)
 y.append(y1)
right = False

for i in range(7):

 for k in range (i + 1, 8):

   if x[i] == x[k] or y[i] == y[k] or abs(x[i] - x[k]) == abs(y[i]-y[k]):

     right = True

if right:

 print("YES")

else:

 print('NO')