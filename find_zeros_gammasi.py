import mpmath
from mpmath import zeta, findroot, mp, re, im, gamma

mp.dps = 50

def zsinh(x, t=0.5):
    z = 1j * x
    return im((zeta(t + z) - zeta(t - z)) / 2)

def gammasi(x, t):
    try:
        z = 1j * x
        return re(1 - gamma(1 - z) / gamma(z))
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
