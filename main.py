from utils import vvv
from Crypto.Util.number import inverse, isPrime

def gcd(a, b):
    vvv(a)
    vvv(b)
    
    if b == 0:
        return a

    q = a//b
    vvv(q)
    vvv()

    return gcd(b, a % b)

def eea(m, b):
    (A1, A2, A3) = (1, 0, m)
    (B1, B2, B3) = (0, 1, b)
    Q = 0

    while True:
        vvv(Q)
        vvv(A1)
        vvv(A2)
        vvv(A3)
        vvv(B1)
        vvv(B2)
        vvv(B3)
        vvv()


        if B3 == 0:
            print('no inverse')
            return A3

        if B3 == 1:
            print('inverse is', B2)
            return B3

        Q = A3 // B3
        (T1, T2, T3) = (A1 - Q * B1, A2 - Q * B2, A3 - Q * B3)
        (A1, A2, A3) = (B1, B2, B3)
        (B1, B2, B3) = (T1, T2, T3)

#gcd(5, 3)
#eea(1759, 553)