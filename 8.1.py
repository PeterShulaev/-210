import math
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx**2 + dy**2)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
result = distance(x1, y1, x2, y2)
print(result)