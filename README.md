# Zeta Based Functions

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

<br />

```math
zeta(0) = zcosh(0, 0) = -1/2
```

<br />

```math
\zeta(t + z) = zcosh(z, t) + zsinh(z, t)
```

```math
\zeta(t - z) = zcosh(z, t) - zsinh(z, t)
```

<br />

```math
\zeta(t + z)\zeta(t - z) = \text{zcosh}^2(z, t) - \text{zsinh}^2(z, t)
```

Graphics zeros zsinh (green), zcosh (blue), t = 0
<img src="https://asyncker.github.io/zeta-function/img/zeros-zsin-zcos.png">

Graphics subtract zeros zsinh (green), zcosh (blue), t = 0
<img src="https://asyncker.github.io/zeta-function/img/zeros-zsin-zcos-sub.png">

The zeros of zsinh(z, t) lie where `Im(ζ(z + t))` <br />
The zeros of zcosh(z, t) lie where `Re(ζ(z + t))` <br />
The zeros of f(x) lie where `Im(ζ(iz) * ζ(-iz))` <br />

Hypothesis:
The roots of the zeta-cosine function consistently become greater than the roots of the zeta-sine function. Does this always hold true for t<1/2? For t=1/2, this rule is violated.

A possible reason for the alternation of zeros: the phase of arg(ζ(it)) changes almost monotonically, its derivative ~= −ln(t/2pi) plus limited fluctuations, and with increasing t, the logarithm suppresses the fluctuations more and more. The zeros of Re (phase ≡ pi/2 mod pi) and the zeros of Im (phase ≡ 0 mod pi) must strictly alternate with a monotonic phase.

<br />

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

See graphics on https://asyncker.github.io/zeta-trigonometry/index.html

define h-function:
```
h(z, w) = ln(z^(-w/2)) = w/2 * ln(1/z) = -w * ln(sqrt(z)) = -w/2 * ln(z)
```

Lambert W/Boltzmann's entropy connection:
```
h(z, -4) = -4/2 * ln(1/z)
```

h₄ = h(2, 4) it's supersymmetry value
```
h(2, 4) = 2 * ln(1/2) = -4 * ln(sqrt(2)) = ln(1/4) = -2 * ln(2)
```

ζ((z^2) ^ (1/2)) + c (c = h(2, 4) = ln(1/4))
<img src="https://raw.githubusercontent.com/asyncker/fractals/refs/heads/main/render/zeta_abs.png">

ζ((z^2) ^ (1/2)) + c (c = h(2, 4) = ln(1/4))
<img src="https://asyncker.github.io/fractals/render/zeta_abs_zoom.png">

zeta function
```
zeta(z) = pow(2pi, z - 1) * sin(z * pi/2) * 2 * gamma(1 - z) * zeta(1 - z)
```

zeta function if use exp and gamma
```
phase = i*pi/2
```

```
zeta(z) = exp((z - 1) * ln(2pi)) * exp(-phase) * (exp(z * phase) - exp(-z * phase)) * gamma(1 - z) * zeta(1 - z)
```

```
sin(z * pi/2) * 2
amplitude: +2, -2
inter: ...-2, +2, −2,    +2, -2, +2...
zeros: ...-6, -4, -2, 0, +2, +4, +6...
```

function
```
1 - conj(z)
```

```
1 - z = -z + 1
```

```
2 * exp(ln(1/2) * z)
```

define tau-function:
```
τ(z) = 1 - exp(1/2 - z)
```

```
τ'(z) = exp(1/2 - z)
```

```
τ'(z) + τ(z) = 1
```

```
τ'(z) / τ(z) = 1 / (exp(z - 1/2) - 1)
```

```
τ(z) * τ(-z) = 1 + e - sqrt(e) * 2 * cosh(z)
τ(z) * τ(-z) = (sqrt(e) - exp(z)) * (sqrt(e) - exp(-z))
τ(iθ) * τ(−iθ) = (1 - sqrt(e))^2 + 4 * sqrt(e) * sin(θ/2)^2
τ(z) - τ(1 - z) = 2 * sinh(z - 1/2)
τ(z) + τ(1 - z) = 2 - 2 * cosh(z - 1/2)
```

test coff:
```
(4 * pi^2) ^ (s - 1) * zeta(s)
```

define mpow:
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
roots(z^2, 2)= +-z
roots(z̄^2, 2) = +-z̄
```

define fold
```
fold(z, k) = (z ^ k) ^ 1/k
folds(z, k) = roots(z ^ k, k)
```

```
folds(z, 2) = +-z
```

<br /> Non-Newton with Multiplicative calculus
If we take the derivative of zsinh using exp, then the function becomes non-closed. The question is, what will the exp derivative tend to if we take it an infinite number of times from zsinh?

```math
L(z) =  \frac{\zeta'(z)}{\zeta(z)}
```

<br />12-adic numbers<br />

```math
\zeta(-1) = -\frac{1}{12} = -0.1_{12}
```

```math
\zeta(0) = -\frac{1}{2} = -0.6_{12}
```

```math
\zeta(2) = \frac{\pi^2}{6} = \pi^2 \cdot 0.2_{12}
```

<br />Non-Archimedean + Hyperreal + p-adic + Laurent Ring<br />
w^-1 = eps <br />
eps^-1 = w <br />
w * eps = 1 <br />

eps and w is the solution of the equation:
1 - eps = 0.999999...
```
(x - 1) * 1/x = 1 - eps 
x = w
```

```
7 / x^2 = eps
x1 = +w * (7 * w) ^ (1/2)
x2 = -w * (7 * w) ^ (1/2)
```

define Φ₆ complex:
```
Φ₆(z, s) = (z^s - 1) * z^s + 1
```

```
Φ₆(z, s) = z^(2s) - z^(1s) + 1

Φ₆(10, 2) = 9901
Φ₆(10, 4) = 99990001
Φ₆(10, 6) = 999999000001
Φ₆(10, 8) = 9999999900000001

33333333333333336666666666666667 = 7 * 13 * 37 * 9901 * 99990001 * 9999999900000001
```

A test to determine whether a number is always composite as n approaches infinity. If possible, determine after what n there will never be any more prime numbers. Ideally, consider n tending to +∞
```
ptlim(10^n) = 0 (n ≥ 0) | ∅
ptlim(2n + 1) = {0, 1} | {1, 2, 3, 5, 6, 8, 9, 11, 14, 15, 18, 20...}
ptlim(10^n + 7) = {0, 1} | {1, 2, 4, 8, 9, 24, 60, 110, 134, 222, 412...}
ptlim(10^(2n) - 10^(1n) + 1) = 0 (n > 8) | {2, 4, 6, 8}
```

```
ln(eps) = -ln(w)
ln(w) = -ln(eps)

ln(w^eps) = -eps * ln(eps)
ln(eps^w) = -w * ln(w)

ln(eps^eps) = -eps * ln(w)
ln(w^w) = -w * ln(eps)

ln(eps * w) = 0
ln(w) / ln(eps) = -1

roots(eps^2, 2) = +-eps
roots(w^2, 2) = +-w

ln(eps^2 + eps^2) * k = ln(2)*k + ln(eps) * 2k
(eps^2 + eps^2) ^ k = 2^k * eps^(2k)

a = 2^n * 5^m (all non-periodic fractions for the 10-adic)

(w - 1) * w + 1 = 999999... 000000... 001.0

3 * 0.333 + 0.001 = 1.0
3 * 0.333333... + eps = 1.0

(w - 1) * 1/w = 0.999999...
(1 - eps) * 1/eps = 999999... 999.000000...
999999... + 0.999999... = 999999... 999.999999... 
```

Scale plane (x-asis it's mult y-asis it's power (example x * eps^y)):<br />
The x-axis is the multiplied coefficient for eps or w  <br />
<img src="https://github.com/asyncker/zeta-function/blob/main/img/scale_plane_algebra.png">
<br />
