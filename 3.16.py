import math
from math import floor

P=int(input())
X=int(input())
Y=int(input())
z = X*100 + Y
k = z + z*P/100
d = k//100
e = k%100
print(d, floor(e))