import mpmath
from mpmath import zeta, findroot, mp, re, im, gamma, fabs, sqrt

mp.dps = 50

def zsinh(x, t=0.5):
    z = 1j * x
    return im((zeta(t + z) - zeta(t - z)) / 2)

def primes_sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = [False] * (((n - i*i) // i) + 1)
    return [i for i, is_prime in enumerate(sieve) if is_prime]

primes = primes_sieve(15551)

def pgamma(z):
    if abs(z) < mp.eps:
        return 1 / z
    result = z # * mp.exp(mp.euler * z)
    for p in primes:
        result *= (1 + z / p) * mp.exp(-z / p)
    return 1 / result

def gammasi(x, t):
    try:
        z = t + 1j * x
        fo = gamma(t - z/2) / gamma(z/2)
        return fo
    except:
        return float('inf')

def gammasi_zeros(x, t=0.5):
    z = t + 1j * x
    return 1 - gamma(t - z/2) / gamma(z/2)

def find_roots(func, funcafter, num_roots=20, step=0.1, t=0.5):
    roots = []
    x = step
    y_prev = funcafter(func(0, t))
    while len(roots) < num_roots:
        y_curr = funcafter(func(x, t))
        if y_prev * y_curr < 0:
            try:
                r = findroot(lambda s: funcafter(func(s, t)), (x-step, x), method='bisect')
                if not roots or abs(r - roots[-1]) > 1e-10:
                    roots.append(r)
            except:
                pass
        x += step
        y_prev = y_curr
    return roots

def find_zeros(func, num_roots=20, step=0.1, t=0.5):
    zeros = []
    x = 0.0
    y_prev = im(func(x, t))
    while len(zeros) < num_roots:
        x += step
        y_curr = im(func(x, t))
        if y_prev * y_curr < 0:
            try:
                r = findroot(lambda s: im(func(s, t)), (x-step, x), method='bisect')
                if abs(re(func(r, t))) < 1e-10:
                    if not zeros or abs(r - zeros[-1]) > 1e-5:
                        zeros.append(r)
            except Exception:
                pass
        y_prev = y_curr
        
    return zeros

roots = find_zeros(gammasi_zeros, 16)
vals = "zeros: "
for r in roots:
    vals += f"{float(r):.7f}, "
print(vals)

roots = find_roots(gammasi, im, 16)
vals = "im: "
for r in roots:
    vals += f"{float(r):.7f}, "
print(vals)

roots = find_roots(gammasi, re, 16)
vals = "re: "
for r in roots:
    vals += f"{float(r):.7f}, "
print(vals)
