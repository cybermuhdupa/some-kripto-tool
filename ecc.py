from Crypto.Util.number import inverse
from collections import namedtuple
from utils import vvv

Point = namedtuple('Point', 'x y')

def add(first, second):
    global p
    return ((first % p) + (second % p)) % p

def subtract(first, second):
    global p
    return (first % p - second % p + p) % p

def multiply(first, second):
    global p
    return ((first % p) * (second % p)) % p

def divide(first, second):
    global p
    return multiply(first, inverse(second, p))

def negative(P):
    return Point(P.x, subtract(0, P.y))

def point_addition(P, Q):
    global p, a

    vvv(P)
    vvv(Q)
    vvv()

    if (P.x == 0 and P.y == 0):
        result = Q
        vvv(result)
        return Q
    if (Q.x == 0 and Q.y == 0):
        result = P
        vvv(result)
        return P
    
    x_p, y_p, x_q, y_q = P.x, P.y, Q.x, Q.y
    
    if (x_p == x_q and (y_p + y_q) % p == 0):
        return Point(0, 0)
    
    vvv(x_p)
    vvv(x_q)
    vvv(y_p)
    vvv(y_q)
    vvv()
    

    if (x_p != x_q or y_p != y_q):
        print('lamb = (%d - %d) / (%d - %d) mod %d' % (y_q, y_p, x_q, x_p, p))
        lamb = divide(subtract(y_q, y_p), subtract(x_q, x_p))
    else:
        print('lamb = (3 * %d * %d + %d) / (2 * %d) mod %d' % (x_p, x_p, a, y_p, p))
        lamb = divide(add(multiply(3, multiply(x_p, x_p)), a), multiply(2, y_p))

    vvv(lamb)
    vvv()
    
    x_r = subtract(subtract(multiply(lamb, lamb), x_p), x_q)
    y_r = subtract(multiply(lamb, subtract(x_p, x_r)), y_p)
    vvv(x_r)
    vvv(y_r)

    return Point(x_r, y_r)

def scalar_multiplication(k, P):
    global Point

    Q = Point(0, 0)
    k = bin(k)[2:]
    
    for k_i in k:
        Q = point_addition(Q, Q)
        if (k_i == '1'):
            Q = point_addition(Q, P)
        
    return Q

def generate_points():
    global E, a, b, p
    for x in range(p):
        vvv(x)
        E_x = E(x)
        vvv(E_x)
        vvv()
    
    for y in range(p):
        vvv(y)
        y_squared = y**2 % p
        vvv(y_squared)
        vvv()

    for x in range(p):
        for y in range(p):
            E_x = E(x)
            y_squared = y**2 % p
            if E_x == y_squared:
                ans = Point(x, y)
                vvv(ans)


p = 23
a = 1
b = 1
assert 4 * (a ** 3) + 27 * (b ** 2) != 0
E = lambda x : (x**3 + a*x + b) % p
P = Point(3, 10)
Q = Point(3, 10)

#point_addition(P, Q)
#generate_points()