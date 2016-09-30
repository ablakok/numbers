import sys
import math

def eratosthenes(n):
    max_prime_factor = math.floor(math.sqrt(n))
    start = 2
    sieve = set(range(start, n + 1))
    while start <= max_prime_factor:
        m = 2 * start
        while m <= n:
            sieve.discard(m)
            m += start
        start = min(x for x in sieve if x > start)
    return sieve

def prime_factors(n):
    remaining = n
    primes = sorted(eratosthenes(n))
    factors = []
    for p in primes:
        a = 0
        while (remaining % p) == 0:
            a += 1
            remaining /= p
        if a > 0:
            factors.append((p, a))
    return factors

def d(n):
    factors = prime_factors(n)
    s = 1
    for (p, a) in factors:
        s *= (a + 1)
    return s

def oldsigma(n):
    return sigma(n) - n

def sigma(n):
    factors = prime_factors(n)
    s = 1
    for (p, a) in factors:
        s *= ((p ** (a + 1) - 1) / (p - 1))
    return int(s)

if __name__ == '__main__':
    input = int(sys.argv[1])
    print(prime_factors(input))
    print(d(input))
    print(sigma(input))
