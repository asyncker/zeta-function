import mpmath
from mpmath import zeta, findroot, mp, re, im, gamma

mp.dps = 50

def primes_sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = [False] * (((n - i*i) // i) + 1)
    return [i for i, is_prime in enumerate(sieve) if is_prime]

primes = primes_sieve(15551)

def pgammaw(z):
    if abs(z) < mp.eps:
        return 1 / z
    result = z * mp.exp(mp.euler * z)
    for n in primes:
        term = (1 + z / n) * mp.exp(-z / n)
        result *= term
    return 1 / result

def gammaw(z, terms=10000):
    if abs(z) < mp.eps:
        return 1 / z
    result = z * mp.exp(mp.euler * z)
    for n in range(1, terms + 1):
        term = (1 + z / n) * mp.exp(-z / n)
        result *= term
    return 1 / result

def zsinh(x, t=0.5):
    z = 1j * x
    return im((zeta(t + z) - zeta(t - z)) / 2)

def gammasi(x, t):
    try:
        z = 1j * x
        return re(1 - gamma(1 - z) / gamma(z))
    except:
        return float('inf')

def pgammasi(x, t):
    try:
        z = 1j * x
        return re(1 - pgamma(1 - z) / pgamma(z))
    except:
        return float('inf')

def find_roots(func, num_roots=20, step=0.1, t=0.5):
    roots = []
    x = step
    y_prev = func(0, t)
    while len(roots) < num_roots:
        y_curr = func(x, t)
        if y_prev * y_curr < 0:
            try:
                r = findroot(lambda s: func(s, t), (x-step, x), method='bisect')
                if not roots or abs(r - roots[-1]) > 1e-10:
                    roots.append(r)
            except:
                pass
        x += step
        y_prev = y_curr
    return roots

roots = find_roots(gammasi, 20)
for r in roots:
    print(1j * r)
