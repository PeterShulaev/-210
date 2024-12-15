N, K = [int(i) for i in input().split()]
elfh = ['I'] * N
for s in range(K):
    left, right = [int(i) for i in input().split()]
    for j in range(left - 1, right):
        elfh[j] = '.'
print(''.join(elfh))