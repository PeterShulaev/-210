def power(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(a, -n)
    else:
        result = 1
        for _ in range(n):
            result *= a
        return result

a = float(input())
n = int(input())
b = power(a, n)
print(b)