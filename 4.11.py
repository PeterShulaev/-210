N = int(input())
a = 0
s = N*(N+1)/2
for i in range(N, 1, -1):
    a = a + int(input())
print(s-a)
