h = int(input())
a = int(input())
b = int(input())
c = 0
t = 1
while c<h:
    c=c+a
    if c>=h:
        print (t)
    else:
        c=c-b
        t=t+1
