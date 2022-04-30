def prob(n):
    days = 500
    res = 1
    for i in range(2, n + 1):
        res *= (days - i + 1) / days
    return 1 - res

n = 2
while prob(n) < 0.5:
    n += 1
print(n, prob(n))