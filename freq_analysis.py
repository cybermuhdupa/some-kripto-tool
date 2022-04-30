f = [
    0.080, 0.015, 0.030, 0.040, 0.130, 0.020, 0.015,
    0.060, 0.065, 0.005, 0.005, 0.035, 0.030,
    0.070, 0.080, 0.020, 0.002, 0.065, 0.060,
    0.090, 0.030, 0.010, 0.015, 0.005, 0.020, 0.002,
]

def p(x):
    return f[(x + 26) % 26]

phi = lambda i : 0.125 * (p(11 - i) + p(13 - i) + p(19 - i) + p(25 - i)) + 0.25 * (p(12 - i) + p(14 - i))

res = []
for i in range(26):
    print(i, '%.4f' % phi(i))
    res.append((phi(i), i))

print()
res = sorted(res)
for x in res:
    print(x[1], '%.4f' % x[0])

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z