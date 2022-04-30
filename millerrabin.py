from random import randint

def miller_rabin(n, a = None, verbose = True):
    if n % 2 == 0:
        if verbose:
            print('Composite - even number')
        return "composite ~ even number"
    k = 0
    q = n - 1
    while q % 2 == 0:
        q //= 2
        k += 1
    if verbose:
        print(f'k: {k}, q: {q}')
    
    if not a:
        a = randint(2, n-1)
    if verbose:
        print(f'a: {a}\n')

    aQ = a ** q
    if verbose:
        print(f'a ^ q: {aQ}')
        print(f'a ^ q mod n: {aQ % n}\n')
    if aQ % n == 1:
        if verbose:
            print("inconclusive")
        return "inconclusive"

    for j in range(k):
        num = a ** ((2 ** j) * q)
        if verbose:
            print(f'a ^ (q * 2 ^ {j}): {num}')
            print(f'a ^ (q * 2 ^ {j}) mod n: {num % n}\n')
        if num % n == n - 1:
            if verbose:
                print('inconclusive')
            return "inconclusive"
    if verbose:
        print('composite')
    return "composite"

miller_rabin(897, 2)
