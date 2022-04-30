k = 0x9087654321ABCDEF

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

state = 0xAA0B675D13ECDD26
state = bin(state)[2:].zfill(64)

IP = (
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 25, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
)

ip = []
for i in range(len(IP)):
    ip.append(IP[i] - 1)

res = ''
for i in range(64):
    res += state[ip[i]]

print()
print(hex(int(res, 2)), res)

print()

expansion = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1,
]

l0 = res[:32]
r0 = res[32:]
print(hex(int(l0, 2)), hex(int(r0, 2)))
print()

r0 = '01000111110110110010011011010010'

eks = ""
for i in range(len(expansion)):
    eks += r0[expansion[i] - 1]
print('eks:', hex(int(eks, 2)))

for i in range(0, len(eks), 6):
    zz = eks[i:i+6]
    print(i // 6 + 1, zz, int(zz[0] + zz[-1], 2), int(zz[1:-1], 2))

hasil_sbox = '00101110010111100001100110100100'
permute = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25,
]
res = ''
for i in range(len(permute)):
    res += hasil_sbox[permute[i] - 1]
print(hex(int(res, 2)), res)