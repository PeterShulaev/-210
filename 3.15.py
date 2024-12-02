import math
from math import floor
a = float(input())
x = (a*120)//3600
print(floor(x))
y = ((a*120)%3600)//60 
print( floor(y))
z = ((a*120)%3600)%60 
print( floor(z))