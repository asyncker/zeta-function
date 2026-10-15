# Zeta Based Functions

Fractals of the zeta: https://asyncker.github.io/zeta-function/zeta_fractal.html

define 0 ± z̄ = fol(z̄, 2) and 1 ± z̄ = 1 + fol(z̄, 2):
```
fol(z, k) = roots(z ^ k, k)
f(z)⁻ = 1 - f(z)
f(z)⁺ = 1 + f(z)
```

define fau, fis, fic:
```
fau(f, z, t, v, a) = (f(t * 2v - z * v) / f(z * v)) * a
fis(f, z, t, v, a) = (f(t * 2v - z * v) - f(z * v)) * a
fic(f, z, t, v, a) = (f(t * 2v - z * v) + f(z * v)) * a
```

```
v = freq (default = 1/2 or 1)
t = shift (default = 1/2 or 0)
a = amp (default = 1/2 or 1)
x = base-power function (default = e or pi)
z = exponent-power function (default = z)
```

define tau, gau, τ, g and hau/hal/har/h:
```
tauₓ(z, t, v) = x^(t * 2v - z * v) / x^(z * v) = x^(t * 2v - z * 2v)
gau(z, t, v) = Γ(t * 2v - z * v) / Γ(z * v)
τₓ(z, t) = x^(t - z)
g(z, t) = Γ(t - z/2) / Γ(z/2)

hau(z, w, t) = (t - w) * ln(z)
hal(z, w, t, v) = (t * 2v - w * v) * ln(z)
har(z, w, v) = (w * v) * ln(z)
h(z, w) = -w/2 * ln(z)
```

Bose-Einstein (-1) and Fermi-Dirac (+1):
```
τ'(z, t)⁻ / τ(z, t)⁻ = +1 / (e^(z - t) - 1)
τ'(z, t)⁺ / τ(z, t)⁺ = -1 / (e^(z - t) + 1)
```

Maxwell–Boltzmann (-0) and Maxwell–Boltzmann (+0):
```
τ'[t](z, t) / τ(z, t) = +1
τ'[z](z, t) / τ(z, t) = -1
```

The zeros lie on Re(z) = 1/2 for any x ∈ N except x = +1
```
τₓ(z, 1/2)⁺⁻ = 1 ± x^(1/2 - z)
```

Visual identity zeta(z) and τ(z, 1/2)⁺⁻:
<table>
  <tr>
    <td><img src="https://asyncker.github.io/zeta-function/img/1-exp(0.5-z).png" alt="1 - exp(1/2 - z)"></td>
    <td><img src="https://asyncker.github.io/zeta-function/img/zeta(z).png" alt="zeta(z)"></td>
    <td><img src="https://asyncker.github.io/zeta-function/img/1+exp(0.5-z).png" alt="1 + exp(1/2 - z)"></td>
  </tr>
  <tr>
    <td align="center"><code>1 - exp(1/2 - z)</code></td>
    <td align="center"><code>zeta(z)</code></td>
    <td align="center"><code>1 + exp(1/2 - z)</code></td>
  </tr>
</table>

```
τ'(z, t)⁻ + τ(z, t)⁻ = 1
τ(z, 1/2)⁻ * τ(-z, 1/2)⁻ = 1 + e - sqrt(e) * 2 * cosh(z) = (sqrt(e) - exp(z)) * (sqrt(e) - exp(-z))
τ(iθ, 1/2)⁻ * τ(−iθ, 1/2)⁻ = (1 - sqrt(e))^2 + 4 * sqrt(e) * sin(θ/2)^2
τ(z, 1/2)⁻ - τ(1 - z, 1/2)⁻ = 0 + 2 * sinh(z - 1/2)
τ(z, 1/2)⁻ + τ(1 - z, 1/2)⁻ = 2 - 2 * cosh(z - 1/2)
u(z, t) = e^(z - t) - 1
u'(z, t) / u(z, t) = 1 / (1 - e^(t - z)) = (1 / (e^(z - t) - 1)) * e^(z - t)

1 / τ(z, t)⁻ = 1 / (1 - e^(t - z))
(z / (1 - exp(t - z)))' = ?
((1 - exp(t - z)) / z)' = ?
g'(z, t)⁻ / g(z, t)⁺ = ?
±f(z, u, t) = u / (t * z^2) * (exp(u / (z * t)) / (exp(u / (z * t)) - 1))

h(z, w)'[w] = -1/2 * ln(z)
h(z, w)'[z] = -w / 2z
h(z, w)'[z] / h(z, w) = 1 / (z * ln(z))
h(z, w) = hau(z, w, w/2)
h(z, w) + h(z, −w) = 0
h(2, 4) = -ln(4) = ln(1/4) = -2 * ln(2)
z^(-w/2) = exp(h(z, w))
z^(-w/2) - z^(w/2) = -2 * sinh(w/2 * ln(z))
z^(-w/2) + z^(w/2) = +2 * cosh(w/2 * ln(z))
```

ζ((z^2)^(1/2)) + c (c = -ln(4))
<img src="https://raw.githubusercontent.com/asyncker/fractals/refs/heads/main/render/zeta_abs.png">

ζ((z^2)^(1/2)) + c (c = -ln(4))
<img src="https://asyncker.github.io/fractals/render/zeta_abs_zoom.png">

```
ζ(±z) - c (c in {2*ln(2), sqrt(2), 2, 2±eps, 1/2, e/2, ~pi/2})
```
ln(4) = 2 * ln(2), which is also the natural logarithm of the entropy of two independent bits. Is it most likely just a numerical coincidence?

τ((z^2)^(1/2), 1/2)⁻
<img src="https://asyncker.github.io/fractals/render/t((w%5E2)%5E(0.5)%2C0.5).png">

zeta(z) and zeta(1 - z):
```
X(z) = zeta(z) / zeta(1 - z)
1 / X(z) = zeta(1 - z) / zeta(z)
X(z) = gamma(1/2 - z/2) / gamma(z/2) * pi^(-1/2 + z)
zeta(z) = gamma(1/2 - z/2) / gamma(z/2) * pi^(-1/2 + z) * zeta(1 - z)
zeta(z) = (2*pi)^(z - 1) * sin(z * pi/2) * 2 * gamma(1 - z) * zeta(1 - z)

X(z) = 2pi^z / (gamma(z/2) * gamma(1 - z/2)) * gamma(1 - z)
X(z) = exp((z - 1) * ln(2pi)) * exp(-i*pi/2) * (exp(z * i*pi/2) - exp(-z * i*pi/2)) * gamma(1 - z)

eta(z) = ((1 - 2^(1-z)) / (1 - 2^z)) * 2^z * pi^(z - 1) * sin(z * pi/2) * gamma(1 - z) * eta(1 - z)
zeta(z) = gamma(1/2 - z/2) / gamma(z/2) * pi^(-1/2 + z) / (1 - 2^z) * eta(1 - z)
zeta(z) = eta(z) / (1 - 2^(1 - z))
```

```
sin(z * pi/2) * 2i = (1 - (-1)^(-z/2)) - (1 - (-1)^(z/2))
sin(z * pi/2) * 2 = ((-1)^(z/2) - (-1)^(-z/2)) * -1i
amplitude: -2, +2
inter: ...-2, +2, −2,    +2, -2, +2...
zeros: ...-6, -4, -2, 0, +2, +4, +6...
1 - (-1)^(-z)
amplitude: 0, +2
```

Hypothesis: all zeros of the 1 - gamma(1/2 - z/2) / gamma(z/2) * pi^(-1/2 + z) with Re(z) > 0 and Re(z) < 1 lie on the critical line Re(z) = 1/2

define cmin, cmax, relumax, relumin, relu-curve ai:
```
cmin(z, w) = min(Re(z), Re(w)) + min(Im(z), Im(w)) * i
cmax(z, w) = max(Re(z), Re(w)) + max(Im(z), Im(w)) * i
cmin(cmax(zeta(z), -1/eps), 1/eps) ~= re(zeta(z))
cmin(cmax(zeta(z) * -i, -1/eps), 1/eps) ~= im(zeta(z))
relumax(z) = cmax(z, 0)
relumin(z) = cmin(z, 0)
relumax(z) + relumin(z) = z
relumax(z) - relumin(z) = +|Re(z)| + |Im(z)|*i
relumin(z) - relumax(z) = -|Re(z)| - |Im(z)|*i
y = ±relumax(log(x^3 - 2x + 2))
```

Empty ◇ means there is no function value at this point. All functions except the equal sign (=) are prohibited, and ◇ is not equal to anything except itself.
```
x = ◇ // float x;
x = 2
relumaxU(z) = z >= +0 ? z : ◇
reluminU(z) = z <= -0 ? z : ◇
```

define mpow (w ∈ ℕ):
```
mpow(z, w) = |z|^w * exp(i * arg(z) * ((1 - exp(i * pi * w)) / 2))
```

A function can be given its cosine (re) and sinus (im) decompositions
```
re(gamma(x + 1i)) it's re-grow
im(gamma(x + 1i)) it's im-grow
re(gamma(1 + xi)) it's re-wave
im(gamma(1 + xi)) it's im-wave
```

define Γₚ, pgamma, gsi, gsiₚ
```math
\frac{1}{\Gammaₚ(z)} = z e^{\gamma z} \prod_{p} \left( 1 + \frac{z}{p} \right) e^{-z/p}
```

```math
\frac{1}{\zeta(z)} = \prod_{p} 1 - p^{-z}
```

```math
\frac{\zeta(z)}{\zeta(2z)} = \prod_{p} 1 + p^{-z}
```

prime-function and eta-function factor:
```
τₚ(z, 0)⁺⁻ = 1 ± p^(0 - z)
τ₂(z, 1)⁻ = 1 - 2^(1 - z)
```

```
gsiₙ(z) = Γₙ(1-z) / Γₙ(z)
gsiₚ(z) = Γₚ(1-z) / Γₚ(z)
```

Hypothesis: all zeros of the gsiₚ(z)⁻ with Re(z) > 0 and Re(z) < 1 lie on the critical line Re(z) = 1/2
```
gsiₙ(z) zeros on 1/2 with natural numbers:
im(gsiₙ(1/2 + it)⁻) = 0 |t={2.7485719, 4.0333153, 5.0685937, 5.9864659, 6.8314286, 7.6251207, 8.3800571, 9.1042716, 9.8032975, 10.4811442, 11.1408316, 11.7847041, 12.4146264, 13.0321124, 13.6384114, 14.2345698, 14.8214748}
re(gsiₙ(1/2 + it)⁻) = 0 |t={2.1497679, 3.3145783, 4.6410998, 5.4849802, 6.4581080, 7.1985308, 8.0367949, 8.7191070, 9.4801506, 10.1233064, 10.8325004, 11.4466874, 12.1178667, 12.7093569, 13.3510553, 13.9240575, 14.5419829}

gsiₚ(z) zeros on 1/2 with prime numbers:
im(gsiₚ(1/2 + it)⁻) = 0 t={1.0293, 5.5865, 9.13, 11.79, 14.13, 16.29, 18.34, 20.29, 22.18, 24.01, 25.89, 27.55, 29.26, 30.95, 32.61, 34.24, 35.86, 37.45, 39.03, 40.6}
re(gsiₚ(1/2 + it)⁻) = 0 t={8.25, 10.00, 13.38, 14.88, 17.64, 19.03, 21.51, 22.84, 25.15, 26.44, 28.63, 29.89, 31.99, 33.22, 35.25, 36.46, 38.44, 39.63, 41.55, 42.73}
```

define zeta‑based functions as symmetric combinations of ζ

```math
\text{zsinh}(z, t) = \frac{\zeta(t + z) - \zeta(t - z)}{2}
```

```math
\text{zcosh}(z, t) = \frac{\zeta(t + z) + \zeta(t - z)}{2}
```

```math
zsinh(-z, t) = −zsinh(z, t)
```

```math
zcosh(-z, t) = zcosh(z, t)
```

```math
\zeta(t + z) = zcosh(z, t) + zsinh(z, t)
```

```math
\zeta(t - z) = zcosh(z, t) - zsinh(z, t)
```

```math
\zeta(t + z)\zeta(t - z) = \text{zcosh}^2(z, t) - \text{zsinh}^2(z, t)
```

<table>
  <tr>
    <td><img src="https://asyncker.github.io/zeta-function/img/zeros-zsin-zcos.png" alt="sin(xₚ)"></td>
    <td><img src="https://asyncker.github.io/zeta-function/img/zeros-zsin-zcos-sub.png" alt="sin(xₙ)"></td>
  </tr>
  <tr>
    <td align="center"><code>zeros zsinh (green), zcosh (blue), t = 0</code></td>
    <td align="center"><code>subtract zeros zsinh (green), zcosh (blue), t = 0</code></td>
  </tr>
</table>
Graphics https://asyncker.github.io/zeta-function/index_graphic.html <br />

The zeros of zsinh(z, t) lie where `Im(ζ(z + t))` <br />
The zeros of zcosh(z, t) lie where `Re(ζ(z + t))` <br />
The zeros of f(x) lie where `Im(ζ(iz) * ζ(-iz))` <br />

Hypothesis:
The roots of the zeta-cosine function consistently become greater than the roots of the zeta-sine function. Does this always hold true for t<1/2? For t=1/2, this rule is violated.

Reason for the alternation of zeros: the phase of arg(ζ(it)) changes almost monotonically, its derivative ~= −ln(t/2pi) plus limited fluctuations, and with increasing t, the logarithm suppresses the fluctuations more and more. The zeros of Re (phase ≡ pi/2 mod pi) and the zeros of Im (phase ≡ 0 mod pi) must strictly alternate with a monotonic phase.

```js
zsinh_zeros[i] < zcosh_zeros[i] // 30k all true except first (t < 1/2)
```

t = 1/2 - 0.00001
```
3.43621400940427, 0.81955124399808, 9.66691026271173, 14.1346623378012, 14.1347267337240, 14.5179833560666, 17.8455997038111,
20.6539992177491, 21.0220373965483, 21.0220842314575, 23.1702821112028, 25.0108287890044, 25.0108610531865, 25.4915386782135,
27.6701825613616, 29.7384907914406, 30.4248701666825, 30.4248929060160, 31.7179796105915, 32.9350461254213, 32.9350680548172,
33.6238113619786, 35.4671838452361, 37.2567074304069, 37.5861751320591, 37.5862111935404, 38.9992117507559, 40.6999543309432,
40.9187169370250, 40.9187671906725, 42.3635472250736, 43.3270600163924, 43.3270808195068, 43.9935435698699
```

```
opErmitor: f1(f(z), f2(f(w̄)))
opDerivit: f1(f'(z), f2(f(w)))
```

define dot, dotlog, dotpow, sop, soplog, soppow:
```
dot(z, w) = z * w̄
dotlog(z, w, k) = log(z * w̄) * k
dotpow(z, w, k) = exp(log(z * w̄) * k)
sop(z, w) = z / w̄
soplog(z, w, k) = log(z / w̄) * k
soppow(z, w, k) = exp(log(z / w̄) * k)
|z| = dotpow(z, z, 1/2)
```

zeta bicomplex 4d with idempotent
```
BL(z) = (z.x - z.w) + (z.y + z.z) * i
BR(z) = (z.x + z.w) + (z.y - z.z) * i
BW(z, w) = 1/2 * (w.x + z.x, z.y + w.y, z.y - w.y, w.x - z.x)
bizeta(z) = BW(ζ(BL(z)), ζ(BR(z)))
```

<img src="https://asyncker.github.io/fractals/render/bicomplex_zeta_near_center.png">

Non-Archimedean + Hyperreal + p-adic + Laurent Ring

Ring two points ±0, ±∞ any graph gamma, 1/x form a continuous and non-tearing curve filling all 1d space. Start 0 or ∞ with shift
```
                ±0 (0)
          -1 (0)    +1 (0)
        -2 (0)        +2 (0)
         .             .
        -2 (∞)        +2 (∞)
          -1 (∞)    +1 (∞)
                ±0 (∞)
```

```
-3 (0), -2 (0), -1 (0), 0 (0), +1 (0), +2 (0), +3 (0)
-3 (∞), -2 (∞), -1 (∞), 0 (∞), +1 (∞), +2 (∞), +3 (∞)

2 + ∞ = 2 (∞)
2 + 0 = 2 (0)
```

define Φ₆ complex:
```
Φ₆(z, w) = 1 + (z^w - 1) * z^w
Φ₆(z, w) = z^(2w) - z^(1w) + 1
Φ₆(10, 2) = 9901
Φ₆(10, 4) = 99990001
Φ₆(10, 6) = 999999000001
Φ₆(10, 8) = 9999999900000001
33333333333333336666666666666667 = 7 * 13 * 37 * 9901 * 99990001 * 9999999900000001
a = 2^n * 5^m (all non-periodic fractions for the 10-adic)
```

add ptlim, count, asymtotic. ptlim - test to see if a number is prime as n approaches +∞ and at what n this ends.
```
ptlim(10^n) = ∅
ptlim(2n + 1) = {1, 2, 3, 5, 6, 8, 9, 11, 14, 15, 18, 20...}
ptlim(10^n + 7) = {1, 2, 4, 8, 9, 24, 60, 110, 134, 222, 412, 700, 999...}
ptlim(10^(2n) - 10^(1n) + 1) = {2, 4, 6, 8}
ptlim(12 * (2^n - 1) - 1) = {1, 3, 4, 7, 9, 12, 15, 16, 25, 37, 40, 43, 49, 72, 75, 124, 180, 196, 208, 312, 480, 568, 1113, 1729, 2244, 3129...}
ptlim(2^n * 3 - 1) = {0, 1, 2, 3, 4, 6, 7, 11, 18, 34, 38, 43, 55, 64, 76, 94, 103, 143, 206, 216, 306, 324, 391, 458, 470, 827, 1274, 3276, 4204, 5134, 7559, 12676, 14898, 18123, 18819, 25690, 26459, 41628, 51387, 71783, 80330, 85687, 88171, 97063, 123630, 155930, 164987, 234760...}
ptlim(2^n * 33 - 65) = {2, 3, 4, 5, 7, 9, 13, 15, 16, 18, 19, 20, 21, 23, 26, 27, 37, 40, 43, 45, 46, 53, 55, 56, 58, 59, 62, 64, 69, 79, 81, 85, 98, 106, 146, 154, 173, 179, 197, 289, 331, 359, 602, 612, 615, 657, 675, 823, 885, 901, 931, 988, 1033, 1039, 1089, 2313, 2671, 3066, 3203, 3813, 4735, 4786, 5114, 5384, 5823, 5832, 6610, 6817, 7800, 10432, 13009, 14802, 18577, 18841, 20612, 23037, 23877, 25673, 27951, 34276, 35656, 36358, 38224...}
ptlim(2^n * 14388 - 12545) = {1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 20, 29, 31, 34, 35, 41, 43, 50, 61, 74, 79, 82, 83, 89, 97, 113, 118, 125, 128, 130, 148, 173, 190, 202, 230, 257, 273, 295, 331, 339, 368, 373, 397, 419, 421, 497, 507, 513, 525, 541, 646, 869, 959, 1302, 1843, 2431, 3103, 3220, 3459, 3947, 4099, 4226, 5241, 5467, 5841, 6531, 6574, 6617, 6669, 6936, 8133, 11145, 12125, 12790, 13115, 15760, 16711, 21593, 27521, 27811, 28367, 29795, 31556, 38861...}

Asymptotic and count function ptlim:
count(ptlim(n)) = pi(n) = count({2, 3, 5, 7, 11, 13, 17...}) = {0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7...}
count(ptlim(n)) ~ ceil(x / (ln(x) - 1))
count(ptlim(2^n - 1)) ~ floor(ln(x) * 2)
count(ptlim(2^n * 33 - 65)) ~ floor(ln(x) * 7)
```

any-adic set coordinate by initial numbers: (naturals, fibbonachi, squares, prime, random and etc.)
```
nₚ = {...-11, -7, -5, -3, -2, 0, +2, +3, +5, +7, +11...}

Re(xₚ) = linear(nₚ) add rational and irrational numbers between primes

for all Re(xₚ) create Re(xₚ) * i its Im(xₚ) get zₚ
```

if use coordinate you get automatic naturals to prime:
```
p-1 = 1, 2, 4, 6, 10, 12, 16, 18, 22... zₚ-1
p*2 = 4, 6, 10, 14, 22, 26, 34... zₚ*2
p^2 = 4, 25, 49, 121, 169... = zₚ^2
2^p = 4, 8, 32, 128, 2048, 8192, 131072... = 2^zₚ
p!  = 2, 6, 120, 5040, 39916800... = gamma(zₚ)
p^p = 4, 27, 3125, 823543, 285311670611... zₚ^zₚ
```

<table>
  <tr>
    <td><img src="https://asyncker.github.io/zeta-function/img/sinprimes.png" alt="sin(xₚ)"></td>
    <td><img src="https://asyncker.github.io/zeta-function/img/sinnaturals.png" alt="sin(xₙ)"></td>
  </tr>
  <tr>
    <td align="center"><code>sin(xₚ) | xₚ = bspline(primes)</code></td>
    <td align="center"><code>sin(xₙ) | xₙ = bspline(naturals)</code></td>
  </tr>
</table>
<table>
  <tr>
    <td><img src="https://asyncker.github.io/zeta-function/img/expprimecoords.png" alt="exp(zₚ)"></td>
    <td><img src="https://asyncker.github.io/zeta-function/img/explinearcoords.png" alt="exp(zₙ)"></td>
  </tr>
  <tr>
    <td align="center"><code>exp(zₚ) + cₚ</code></td>
    <td align="center"><code>exp(zₙ) + cₙ</code></td>
  </tr>
</table>
<table>
  <tr>
    <td><img src="https://asyncker.github.io/zeta-function/img/expprimecoordjulia.png" alt="exp(zₚ)"></td>
    <td><img src="https://asyncker.github.io/zeta-function/img/explinearcoordjulia.png" alt="exp(zₙ)"></td>
  </tr>
  <tr>
    <td align="center"><code>exp(zₚ) (scale 1:1)</code></td>
    <td align="center"><code>exp(zₙ) (scale 1:1)</code></td>
  </tr>
</table>

family of gamma (if x<0 switch sign {-1, +1} to {+1, -1} in prime, random, etc.), exp (2pi * prime, 2pi * random, etc.)
```
Γ(z, s = {2, 3, 5, 7...}) = 1 / (z · e^γz · ∏ₛ((1 + z/n) · e^(−z/n)))
e(z, s = {2, 3, 5, 7...}) = 
```

epsilon and omega numbers:
```
eps = 1 - 0.999999... (eps ≠ 0)
eps^-1 = w
w^-1 = eps
```

```
(x - 1) * 1/x = 1 - eps 
x = w

7 / x^2 = eps
x = ±w * (7 * w) ^ (1/2)
```

```
w * eps = 1
ln(eps) = -ln(w)
ln(w) = -ln(eps)

ln(w^eps) = -eps * ln(eps)
ln(eps^w) = -w * ln(w)
ln(eps^eps) = -eps * ln(w)
ln(w^w) = -w * ln(eps)
ln(eps^2 + eps^2) * k = ln(2)*k + ln(eps) * 2k
(eps^2 + eps^2) ^ k = 2^k * eps^(2k)
roots(eps^2, 2) = ±eps

sym(x) = (|f(x - eps)| + |f(x + eps)|) / 2
signs(x) = { sign(f(x - eps)), sign(f(x + eps)) }; // {-, -} {-, +} {+, -} {+, +}
signs(gamma(-1)) = {+, -}
signs(gamma(-0)) = {-, +}
signs(1 / 0) = {-, +}
(|gamma(-0 - eps)| + |gamma(-0 + eps)|) / 2 = ~(1/eps + eps)

3 * 0.333 + 0.001 = 1.0
3 * 0.333333... + eps = 1.0
(w - 1) * w + 1 = 999999... 000000... 001.0
(w - 1) * 1/w = 0.999999...
(1 - eps) * 1/eps = 999999... 999.000000...
999999... + 0.999999... = 999999... 999.999999... 
```

Scale plane (x-asis it's mult coefficient for eps or w y-asis it's power (example x * eps^y)):<br />
<img src="https://asyncker.github.io/fractals/render/scale_plane_algebra.png">
