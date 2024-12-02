A = int(input())
B = int(input())
if A>=0 and B>=0:
    if A<B:
        for i in range(A, B+1):
            print(i, end=' ')
    elif A==B:
        print(A)
    elif A>B:
        for i in range(-A, B-1):  
            print(abs(i), end=' ')
elif A<0 and B<0:
    if A<B:
        for i in range(A, B+1):
            print(i, end=' ')
    elif A==B:
        print(A)
    elif A>B:
        for i in range(abs(A), abs(B-1)):  
            print((-i), end=' ')
elif A<0 and B>0:
    for i in range(A, B+1):
        print(i)
elif A>0 and B<0:
    for i in range(A, (B-1), -1):
        print(i, end=' ')
