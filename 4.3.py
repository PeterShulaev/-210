A = int(input())
B = int(input())
for i in range(A, B-1, -1):
    if i%2==1:
        print(i)
        
    i=i-1
