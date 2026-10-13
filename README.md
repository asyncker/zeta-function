# Zeta Based Functions

Fractals of the zeta: https://asyncker.github.io/zeta-function/zeta_fractal.html

define folds
```
fold(z, k) = (z ^ k) ^ 1/k
folds(z, k) = roots(z ^ k, k)
```

```
folds(z, 2) = ±z
folds(z̄, 2) = ±z̄
```

define 1 - z = msub(z) and 1 + z = madd(z):
```
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
v = freq (default = 1/2)
t = shift (default = 1/2 or 0)
a = amp (default = 1/2 or 1)
x = base-power function (default = e)
z = exponent-power function (default = z)
```

define tau, gau, τ, g and hau/hal/har:
```
tauₓ(z, t, v) = x^(t * 2v - z * v) / x^(z * v)
gau(z, t, v) = Γ(t * 2v - z * v) / Γ(z * v)
τₓ(z, t) = x^(t - z)
g(z, t) = Γ(t - z/2) / Γ(z/2)

hau(z, w, t) = (t - w) * ln(z)
hal(z, w, t, v) = (t * 2v - w * v) * ln(z)
har(z, w, v) = (w * v) * ln(z)
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

The zeros lie on Re(w) = 1/2 for any x ∈ N except x = +1
```
τₓ(z, 1/2)⁺⁻ = 1 ± x^(1/2 - z)
```

Any-adic numbers:

family of gamma functions (if x<0 switch sign {-1, +1} to {+1, -1} period prime numbers or fibonachi numbers or 2, 4, 8, 16, 32... or random numbers or any sequance)
```
Γ(z, s = {2, 3, 5, 7...}) = 1 / (z · e^γz · ∏ₛ((1 + z/n) · e^(−z/n)))
```

family of exp functions (period 2pi * prime or fibonachi numbers or 2, 4, 8, 16, 32... or random numbers or any sequance)
```
e(z, s = {2, 3, 5, 7...}) = 
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
1 / τ(z, t)⁻ = 1 / (1 - e^(t - z))
```

```
τ'(z, t)⁻ = exp(t - z)
(z / τ(z, t)⁻)' =
(τ(z)⁻ / z)' =
g'(z, t)⁻ / g(z, t)⁺ = 

u(z, t) = e^(z - t) - 1
u'(z, t) / u(z, t) = 1 / (1 - e^(t - z)) = (1 / (e^(w - t) - 1)) * e^(w - t)
```

```
τ'(z)⁻ + τ(z)⁻ = 1
τ(z)⁻ * τ(-z)⁻ = 1 + e - sqrt(e) * 2 * cosh(z)
τ(z)⁻ * τ(-z)⁻ = (sqrt(e) - exp(z)) * (sqrt(e) - exp(-z))
τ(iθ)⁻ * τ(−iθ)⁻ = (1 - sqrt(e))^2 + 4 * sqrt(e) * sin(θ/2)^2
τ(z)⁻ - τ(1 - z)⁻ = 2 * sinh(z - 1/2)
τ(z)⁻ + τ(1 - z)⁻ = 2 - 2 * cosh(z - 1/2)
```

prime-function and eta-function factor:
```
τₚ(z, 0)⁺⁻ = 1 ± p^(0 - z)
τ₂(z, 1)⁻ = 1 - 2^(1 - z)

re: ∏(1 + p^-z) = zeta(z) / zeta(2z)
im: ∏(1 - p^-z) = 1 / zeta(z)
```

define h-function
```
h(z, w) = -w/2 * ln(z)
```

```
h(z, w) + h(z, −w) = 0
h(z, w)'[w] = -1/2 * ln(z)
h(z, w)'[z] = -w / 2z
h(z, w)'[z] / h(z, w) = 1 / (z * ln(z))
exp(hau(z, w, w/2)) = z^(-w/2)
```

```
e^(-w/2 * ln(z)) + e^(w/2 * ln(z)) = 2 * cosh(w/2 * ln(z))
e^(-w/2 * ln(z)) - e^(w/2 * ln(z)) = 2 * sinh(w/2 * ln(z))
```

```
f(z, u, t) = 0 ± (u / (t * z^2) * (exp(u / (z * t)) / (exp(u / (z * t)) - 1)))
```

ζ((z^2) ^ (1/2)) + c (c = -ln(4))
<img src="https://raw.githubusercontent.com/asyncker/fractals/refs/heads/main/render/zeta_abs.png">

ζ((z^2) ^ (1/2)) + c (c = -ln(4))
<img src="https://asyncker.github.io/fractals/render/zeta_abs_zoom.png">

ln(4) = 2 * ln(2) which is also the natural-log entropy of two independent bits, I wonder whether this is merely a numerical coincidence or whether there is a genuine connection between the zeta function, the constant ln(4), and two-bit entropy.

supersymmetry value:
```
h(2, 4) = -ln(4) = ln(1/4) = -2 * ln(2)
```

1 - exp(1/2 - (|Re(z)| + |Im(z)| * i)) | τ(±z, 1/2)⁻
<img src="https://asyncker.github.io/fractals/render/t((w%5E2)%5E(0.5)%2C0.5).png">

zeta(z) and zeta(1 - z) function:
```
zeta(z) = pow(2pi, z - 1) * sin(z * pi/2) * 2 * gamma(1 - z) * zeta(1 - z)
zeta(z) = gamma(1/2 - z/2) / gamma(z/2) * pi^(-1/2 + z) * zeta(1 - z)
zeta(1 - z) = gamma(z/2) / gamma(1/2 - z/2) * pi^(1/2 - z) * zeta(z)
```

zeta function if use exp and gamma:
```
phase = i*pi/2
zeta(z) = exp((z - 1) * ln(2pi)) * exp(-phase) * (exp(z * phase) - exp(-z * phase)) * gamma(1 - z) * zeta(1 - z)
```

zeta function if use gamma:
```
zeta(z) = 2pi^z / (gamma(z/2) * gamma(1 - z/2)) * gamma(1 - z) * zeta(1 - z)
```

zeta function if use eta function:
```
zeta(z) = 2pi^(z - 1) * sin(z * pi/2) * 2 * gamma(1 - z) / (1 - 2^z) * eta(1 - z)
zeta(z) = gamma(1/2 - z/2) / gamma(z/2) * pi^(-1/2 + z) / (1 - 2^z) * eta(1 - z)
zeta(z) = eta(z) / (1 - 2^(1 - z))
```

eta function:
```
eta(z) = ((1 - 2^(1-z)) / (1 - 2 ^ z)) * 2^z * pi^(z - 1) * sin(z * pi/2) * gamma(1 - z) * eta(1 - z)
```

zeta function symetric:
```
zeta(z) / zeta(1 - z) = gamma(1/2 - z/2) / gamma(z/2) * pi^(-1/2 + z)
zeta(1 - z) / zeta(z) = 1 / (zeta(z) / zeta(1 - z))
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

```
t = 1/2 & v = 1/2
1 - gamma(t * 2v - z * v) / gamma(z * v)
1 - exp(t * 2v - z * v) / exp(z * v) = 1 - exp(t * 2v - z * 2v)
1 - gamma(1/2 - z/2) / gamma(z/2)
```

define relumax, relumin, relu-curve ai:
```
relumax(x) = max(x, 0)
relumin(x) = min(x, 0)
y1 = +relumax(log(x^3 - 2x + 2))
y2 = -relumin(log(x^3 - 2x + 2))
relumax(z) + relumin(z) = ?
relumax(z) - relumin(z) = ?
relumin(z) + relumax(z) = ?
relumin(z) - relumax(z) = ?
```

Empty for relu-curve:
◇ means there is no function value at this point. All functions except the equal sign (=) are prohibited, and ◇ is not equal to anything except itself. You can write x = ◇
```
x = ◇ // float x;
x = 2
relumaxU(z) = z >= +0 ? z : ◇
reluminU(z) = z <= -0 ? z : ◇
```

```
cmin(z, w) = min(z.x, w.x) + min(z.i, w.i) * i
cmax(z, w) = max(z.x, w.x) + max(z.i, w.i) * i
w = 1 / eps
cmin(cmax(zeta(z), -w), w) ~= re(zeta(z))
cmin(cmax(zeta(z) * -i, -w), w) ~= im(zeta(z))
```

A function can be given its cosine (re) and sinus (im) decompositions
```
re(gamma(x + 1i)) it's cos-grow
im(gamma(x + 1i)) it's sin-grow
re(gamma(1 + xi)) it's cos-wave
im(gamma(1 + xi)) it's sin-wave
gamma(w + z) = ??
```

define Γₚ, pgamma, gsi, gsiₚ
```math
\frac{1}{\Gammaₚ(z)} = z e^{\gamma z} \prod_{p} \left( 1 + \frac{z}{p} \right) e^{-z/p}
```

```math
\frac{1}{\zeta(z)} = \prod_{p} 1 - p^{-s}
```

```
gsi(z) = Γ(1-z) / Γ(z)
gsiₚ(z) = Γₚ(1-z) / Γₚ(z)
```

Hypothesis: all zeros of the gsiₚ(z)⁻ with Re(z) > 0 and Re(z) < 1 lie on the critical line Re(z) = 1/2

If Re(z) >= 1 infinity zeros and Re(z) <= 0 infinity zeros

gsiₙ(z) zeros on 1/2 with natural numbers:
```
im(gsiₙ(1/2 + it)⁻) = {2.7485719, 4.0333153, 5.0685937, 5.9864659, 6.8314286, 7.6251207, 8.3800571, 9.1042716, 9.8032975, 10.4811442, 11.1408316, 11.7847041, 12.4146264, 13.0321124, 13.6384114, 14.2345698, 14.8214748}
re(gsiₙ(1/2 + it)⁻) = {2.1497679, 3.3145783, 4.6410998, 5.4849802, 6.4581080, 7.1985308, 8.0367949, 8.7191070, 9.4801506, 10.1233064, 10.8325004, 11.4466874, 12.1178667, 12.7093569, 13.3510553, 13.9240575, 14.5419829}
```

gsiₚ(z) zeros on 1/2 with prime numbers:
```
im(gsiₚ(1/2 + it)⁻) = {1.0293, 5.5865, 9.13, 11.79, 14.13, 16.29, 18.34, 20.29, 22.18, 24.01, 25.89, 27.55, 29.26, 30.95, 32.61, 34.24, 35.86, 37.45, 39.03, 40.6}
re(gsiₚ(1/2 + it)⁻) = {8.25, 10.00, 13.38, 14.88, 17.64, 19.03, 21.51, 22.84, 25.15, 26.44, 28.63, 29.89, 31.99, 33.22, 35.25, 36.46, 38.44, 39.63, 41.55, 42.73}
```

define 3-symetryics of f(z):
```
opErmitor: f1(f(z), f2(f(w̄)))
opSymetri: 1 - f1(f(1 - z), f2(f(w)))
opDerivit: f1(f'(z), f2(f(w)))
```

define mpow (w ∈ ℕ):
```
mpow(z, w) = |z|^w * exp(i * arg(z) * ((1 - exp(i * pi * w)) / 2))
```

define dot, dotlog, dotpow:
```
dot(z, w) = z * w̄
dotlog(z, w, k) = log(z * w̄) * k
dotpow(z, w, k) = exp(log(z * w̄) * k)
```

```
|z| = dotpow(z, z, 1/2)
|z|^2 = dotpow(z, z, 1)
|z|^(1/2) = dotpow(z, z, 1/4)
1 / |z| = dotpow(z, z, -1/2)
1 / |z|^2 = dotpow(z, z, -1)
1 / |z|^(1/2) = dotpow(z, z, -1/4)

log(|z|) = dotlog(z, z, 1/2)
log(|z|^2) = dotlog(z, z, 1)
log(|z|^(1/2)) = dotlog(z, z, 1/4)
log(1 / |z|) = dotlog(z, z, -1/2)
log(1 / |z|^2) = dotlog(z, z, -1)
log(1 / |z|^(1/2)) = dotlog(z, z, -1/4)
```

```
(re(z)^2)^0.5 + (im(z)^2)^0.5*i = |re(z)| + |im(z)|*i
```

define sop function:
```
sop(z, w) = z / w̄
soplog(z, w, k) = log(z / w̄) * k
soppow(z, w, k) = exp(log(z / w̄) * k)
```

Define zeta‑based functions as symmetric combinations of ζ

```math
\text{zsinh}(z, t) = \frac{\zeta(t + z) - \zeta(t - z)}{2}
```

```math
\text{zcosh}(z, t) = \frac{\zeta(t + z) + \zeta(t - z)}{2}
```

<br />

```math
zsinh(-z, t) = −zsinh(z, t)
```

```math
zcosh(-z, t) = zcosh(z, t)
```

```math
zeta(0) = zcosh(0, 0) = -1/2
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
Graphics https://asyncker.github.io/zeta-function/index_graphic.html

The zeros of zsinh(z, t) lie where `Im(ζ(z + t))` <br />
The zeros of zcosh(z, t) lie where `Re(ζ(z + t))` <br />
The zeros of f(x) lie where `Im(ζ(iz) * ζ(-iz))` <br />

Hypothesis:
The roots of the zeta-cosine function consistently become greater than the roots of the zeta-sine function. Does this always hold true for t<1/2? For t=1/2, this rule is violated.

A possible reason for the alternation of zeros: the phase of arg(ζ(it)) changes almost monotonically, its derivative ~= −ln(t/2pi) plus limited fluctuations, and with increasing t, the logarithm suppresses the fluctuations more and more. The zeros of Re (phase ≡ pi/2 mod pi) and the zeros of Im (phase ≡ 0 mod pi) must strictly alternate with a monotonic phase.

```js
for (let i = 1; i < 30001; i++) {
    console.log(zsinh_zeros[i] < zcosh_zeros[i]); // 30k all true except first (t < 1/2)
}
```

t = 1/2 - 0.00001
```
3.4362140094042727618286113340360934506738787548597
0.81955124399808421306572241644739516686114223957193
9.6669102627117306193907187588664936887949596215645
14.134662337801231264783053269158275738710128737448
14.134726733724055751480138987456071685484173664554
14.517983356066677772850986295374471471504560789106
17.845599703811184951957455484942204619177185074612
20.653999217749134085058454969275268894937808726164
21.02203739654834299714967714165155496392643807671
21.022084231457519055805725702330275768340332172454
23.170282111202890685442669367056156070470219974683
25.010828789004412269219485233798903561212641473613
25.010861053186551215744803766770051137486731602211
25.491538678213580294714236283761598679995916554608
27.670182561361602782851655303702441139160483133524
29.73849079144066595737146108224554545677766612479
30.424870166682584655140590167156737977280411006862
30.424892906016094362582098054973313769120166261422
31.717979610591542422557982339162944429686986670321
32.935046125421386611939970592960966749639178172335
32.935068054817277516882556456005962651681505304866
33.623811361978644055405727771675330758287407611779
35.467183845236152462050553677145271567623651763461
37.256707430406954377867175959115064714845313075613
37.58617513205913039355349678786077986646323345893
37.586211193540447475725879238644740485553842623415
38.999211750755936474251225763996381489068026232462
40.699954330943242482880179099883335971831730455691
40.918716937025009960905850723200193925507298193954
40.918767190672526549033451184587165342387577520953
42.363547225073666641078295652543590243704687852681
43.327060016392470396194201535206695150214060963441
43.327080819506881636510075116474719722187763198857
43.993543569869915147558964285592053160826471283816
```

<br /> Zeta Bicomplex 4d

Use idempotent function:
```
BL(z) = (z.x - z.w) + (z.y + z.z) * i
BR(z) = (z.x + z.w) + (z.y - z.z) * i
BW(z, w) = 1/2 * (w.x + z.x, z.y + w.y, z.y - w.y, w.x - z.x)
bizeta(z) = BW(ζ(BL(z)), ζ(BR(z)))
```

<img src="https://asyncker.github.io/fractals/render/bicomplex_zeta_near_center.png">

<br />Non-Archimedean + Hyperreal + p-adic + Laurent Ring<br />
```
eps = 1 - 0.999999... (eps ≠ 0)
eps^-1 = w
w^-1 = eps
w * eps = 1
```

eps and w is the solution of the equation:
```
(x - 1) * 1/x = 1 - eps 
x = w
```

```
7 / x^2 = eps
x1 = +w * (7 * w) ^ (1/2)
x2 = -w * (7 * w) ^ (1/2)
```

All real numbers form a ring and two points ±0 and ±inf any graph including gamma and 1/x form a continuous and non-tearing curve filling all 1d space.<br />
Starting point and shift
```
                ±0 (0)
          -1 (0)    +1 (0)
        -2 (0)        +2 (0)
         .             .
        -2 (∞)        +2 (∞)
          -1 (∞)    +1 (∞)
                ±0 (∞)
```

Start 0 and invert ∞ with shift
```
-3 (0), -2 (0), -1 (0), 0 (0), +1 (0), +2 (0), +3 (0)
-3 (∞), -2 (∞), -1 (∞), 0 (∞), +1 (∞), +2 (∞), +3 (∞)
```

```
2 + ∞ = 2 (∞)
2 + 0 = 2 (0)
```

all non-periodic fractions for the 10-adic
```
a = 2^n * 5^m
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
```

add function ptlim, count, asymtotic. A test to determine whether a number is always composite as n approaches infinity. If possible, determine after what n there will never be any more prime numbers. Ideally, consider n tending to +∞
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

<br />Coordinate by sequence:

We use any set as initial coordinates (naturals, fibbonachi, squares, prime, random)
```
xₚ = {...-11, -7, -5, -3, -2, 0, +2, +3, +5, +7, +11...}

Re(xₚ) = linear(xₚ) add rational and irrational numbers between primes

for all Re(xₚ) create Re(xₚ) * i its Im(xₚ)
```

If use Coordinate by sequence idea. You get automatic naturals to prime:
```
p^2 = 4, 25, 49, 121, 169... = zₚ^2
p! = 2, 6, 120, 5040, 39916800... = gamma(zₚ)
2^p = 4, 8, 32, 128, 2048, 8192, 131072... = 2^zₚ
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

```
ln(eps) = -ln(w)
ln(w) = -ln(eps)

ln(w^eps) = -eps * ln(eps)
ln(eps^w) = -w * ln(w)
ln(eps^eps) = -eps * ln(w)
ln(w^w) = -w * ln(eps)

ln(eps * w) = 0
ln(w) / ln(eps) = -1

sym(x) = (|f(x - eps)| + |f(x + eps)|) / 2
sig(x) = { sign(f(x - eps)), sign(f(x + eps)) }; // {-, -} {-, +} {+, -} {+, +}

(|gamma(-2.0 - eps)| + |gamma(-2.0 + eps)|) / 2 = {-, +}
(|gamma(-1.0 - eps)| + |gamma(-1.0 + eps)|) / 2 = {+, -}
(|gamma(-0.0 - eps)| + |gamma(-0.0 + eps)|) / 2 = {-, +}
(|1/(-0.0 - eps)| + |1/(-0.0 + eps)|) / 2 = {-, +}

roots(eps^2, 2) = +-eps
roots(w^2, 2) = +-w

ln(eps^2 + eps^2) * k = ln(2)*k + ln(eps) * 2k
(eps^2 + eps^2) ^ k = 2^k * eps^(2k)

(w - 1) * w + 1 = 999999... 000000... 001.0

3 * 0.333 + 0.001 = 1.0
3 * 0.333333... + eps = 1.0

(w - 1) * 1/w = 0.999999...
(1 - eps) * 1/eps = 999999... 999.000000...
999999... + 0.999999... = 999999... 999.999999... 
```

Scale plane (x-asis it's mult y-asis it's power (example x * eps^y)):<br />
The x-axis is the multiplied coefficient for eps or w  <br />
<img src="https://asyncker.github.io/fractals/render/scale_plane_algebra.png">
