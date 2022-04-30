k = 0xAA930D781C65442F

bin_k = bin(k)[2:].zfill(64)
for i in range(0, len(bin_k), 10):
    print(i, bin_k[i:i+10])
print()

pc1_c0 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
]

pc1_d0 = [
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4,
]

c0 = ""
d0 = ""
for i in range(len(pc1_c0)):
    c0 += bin_k[pc1_c0[i] - 1]
    d0 += bin_k[pc1_d0[i] - 1]
print('c0 =', c0)
print('d0 =', d0)

pc2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32,
]

c1 = c0[1:] + c0[0]
d1 = d0[1:] + d0[0]
print('c1 =', c1)
print('d1 =', d1)

res = c1 + d1
k1 = ""
for i in range(len(pc2)):
    k1 += res[pc2[i] - 1]
print('k1 =', k1, hex(int(k1, 2))[2:].upper().zfill(12))

print()

c2 = c1[1:] + c1[0]
d2 = d1[1:] + d1[0]
print('c2 =', c2)
print('d2 =', d2)

res = c2 + d2
k2 = ""
for i in range(len(pc2)):
    k2 += res[pc2[i] - 1]
print('k2 =', k2, hex(int(k2, 2))[2:].upper().zfill(12))

print()

c3 = c2[2:] + c2[:2]
d3 = d2[2:] + d2[:2]
print('c3 =', c3)
print('d3 =', d3)

res = c3 + d3
k3 = ""
for i in range(len(pc2)):
    k3 += res[pc2[i] - 1]
print('k3 =', k3, hex(int(k3, 2))[2:].upper().zfill(12))
