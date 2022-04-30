# This is a modified version of boppreh's AES implementation found at at https://github.com/boppreh/AES
# With modification for verbosity in its step

from Crypto.Util.number import long_to_bytes, bytes_to_long
from utils import vvv, vvvbytes, bbb
import inspect, re

# notes: block length = 16 bytes
# key length = 16 bytes
# if first byte is zero, then we should add it manually to pass the assertion
plaintext = 0x5A6C730ABCFED7712300784901234567
key = 0x13AE78063E9244ED5AD45689BCB01234

plaintext = long_to_bytes(plaintext)
key = long_to_bytes(key)
assert(len(plaintext) == 16)
assert(len(key) == 16)

vvvbytes(plaintext)
vvvbytes(key)
vvv()

def printmatrix(arg):
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        m = re.search(r'\bprintmatrix\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            name = m.group(1)
            break
    
    print(name, '=')
    row_0 = arg[0]
    row_1 = arg[1]
    row_2 = arg[2]
    row_3 = arg[3]

    vvvbytes(row_0)
    vvvbytes(row_1)
    vvvbytes(row_2)
    vvvbytes(row_3)
    print()

state = [
    [plaintext[0], plaintext[4], plaintext[8], plaintext[12]],
    [plaintext[1], plaintext[5], plaintext[9], plaintext[13]],
    [plaintext[2], plaintext[6], plaintext[10], plaintext[14]],
    [plaintext[3], plaintext[7], plaintext[11], plaintext[15]],
]

round_key = [
    [key[0], key[4], key[8], key[12]],
    [key[1], key[5], key[9], key[13]],
    [key[2], key[6], key[10], key[14]],
    [key[3], key[7], key[11], key[15]],
]

printmatrix(state)
printmatrix(round_key)

s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

r_con = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36,
)

def sub_bytes(s):
    for i in range(4):
        for j in range(4):
            s[i][j] = s_box[s[i][j]]
    return s

def get_w(m, col):
    return bytearray([m[0][col], m[1][col], m[2][col], m[3][col]])

def g_box(w, rnd):
    print('g_box =')
    vvvbytes(w)

    RotWord = bytearray([w[1], w[2], w[3], w[0]])
    vvvbytes(RotWord)

    SubWord = bytearray([s_box[RotWord[i]] for i in range(4)])
    vvvbytes(SubWord)

    Rcon = r_con[rnd]
    print('Rcon(%d) =' % rnd, str(Rcon).zfill(2), '00 00 00')

    result = bytearray([Rcon ^ SubWord[0], SubWord[1], SubWord[2], SubWord[3]])
    vvvbytes(result)
    vvv()
    return result

print('round key 0')
for j in range(4):
    print('w(%d) = ' % j, end='')
    print(bbb(get_w(round_key, j)))
vvv()

def xorlist(a, b):
    return [i^j for i, j in zip(a, b)]

def xormatrix(a, b):
    c = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    for i in range(4):
        for j in range(4):
            c[i][j] = a[i][j] ^ b[i][j]
    return c

def shift_rows(s):
    s[1][0], s[1][1], s[1][2], s[1][3] = s[1][1], s[1][2], s[1][3], s[1][0]
    s[2][0], s[2][1], s[2][2], s[2][3] = s[2][2], s[2][3], s[2][0], s[2][1]
    s[3][0], s[3][1], s[3][2], s[3][3] = s[3][3], s[3][0], s[3][1], s[3][2]
    return s

# learned from http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

def mix_single_column(a):
    # see Sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)
    return a

def mix_columns(s):
    res = []
    for i in range(4):
        res.append(mix_single_column(get_w(s, i)))
    
    res_transpose = [get_w(res, i) for i in range(4)]
    return res_transpose

for i in range(1, 2):
    print('round:', i)
    start_round = xormatrix(state, round_key)

    printmatrix(start_round)
    
    after_subbytes = sub_bytes(start_round)
    printmatrix(after_subbytes)

    after_shiftrows = shift_rows(after_subbytes)
    printmatrix(after_shiftrows)

    if i < 10:
        after_mixcolumns = mix_columns(after_shiftrows)
        printmatrix(after_mixcolumns)
        state = after_mixcolumns
    else:
        state = after_shiftrows

    print('calculate round key %d ...' % i)

    new_w_0 = g_box(get_w(round_key, 3), i)
    
    new_w_1 = xorlist(get_w(round_key, 0), new_w_0)
    new_w_2 = xorlist(get_w(round_key, 1), new_w_1)
    new_w_3 = xorlist(get_w(round_key, 2), new_w_2)
    new_w_4 = xorlist(get_w(round_key, 3), new_w_3)

    round_key = [
        [new_w_1[0], new_w_2[0], new_w_3[0], new_w_4[0]],
        [new_w_1[1], new_w_2[1], new_w_3[1], new_w_4[1]],
        [new_w_1[2], new_w_2[2], new_w_3[2], new_w_4[2]],
        [new_w_1[3], new_w_2[3], new_w_3[3], new_w_4[3]],
    ]

    print('round key %d' % i)
    for j in range(4 * i, 4 * i + 4):
        print('w(%d) = ' % j, end='')
        print(bbb(get_w(round_key, j % 4)))
    vvv()

add_round_key = xormatrix(state, round_key)
printmatrix(add_round_key)