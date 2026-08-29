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

See graphics on https://asyncker.github.io/zeta-function/index_graphic.html

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

define tau-function and hau-function:
```
tau(z, w, t, a)⁺⁻ = a ± z^(t - w)
```

```
hau(z, w, t) = (t - w) * ln(z)
```

```
τ(w, t)⁺⁻ = 1 ± e^(t - w)
```

Bose-Einstein:
```
τ'(w, t)⁻ / τ(w, t)⁻ = 1 / (e^(w - t) - 1)
```

Fermi-Dirac:
```
τ'(w, t)⁺ / τ(w, t)⁺ = -1 / (e^(w - t) + 1)
```

Visual identity zeta(z) and τ(w, 1/2)⁺⁻:

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
τ'(w, t)⁻ = exp(t - w)
-1 / τ(w)⁻
(w / τ(w))'
(τ(w) / w)'


u(z, t) = e^(z - t) - 1
u'(z, t) / u(z, t) = 1 / (1 - e^(t - z)) = (1 / (e^(w - t) - 1)) * e^(w - t)
```

```
τ'(w)⁻ + τ(w)⁻ = 1
τ(w)⁻ * τ(-w)⁻ = 1 + e - sqrt(e) * 2 * cosh(w)
τ(w)⁻ * τ(-w)⁻ = (sqrt(e) - exp(w)) * (sqrt(e) - exp(-w))
τ(iθ)⁻ * τ(−iθ)⁻ = (1 - sqrt(e))^2 + 4 * sqrt(e) * sin(θ/2)^2
τ(w)⁻ - τ(1 - w)⁻ = 2 * sinh(w - 1/2)
τ(w)⁻ + τ(1 - w)⁻ = 2 - 2 * cosh(w - 1/2)
```

eta-function factor:
```
τ₂(w, 1)⁻ = 1 - 2^(1 - w)
```

prime-function factor:
```
τₚ(w, 0)⁺⁻ = 1 ± p^(0 - w)

re: ∏(1 + p^-s) = zeta(s) / zeta(2s)
im: ∏(1 - p^-s) = 1 / zeta(s)
```

define h-function (with Lambert W/Boltzmann's entropy connection)
```
h(z, w) = -w/2 * ln(z)
```

```
h(z, w) + h(z, −w) = 0
```

```
D¹[w](h(z, w)) = -1/2 * ln(z)
```

```
D¹[z](h(z, w)) = -w / 2z
D¹[z](h(z, w)) / h(z, w) = 1 / (z * ln(z))
```

```
e^(-w/2 * ln(z)) + e^(w/2 * ln(z)) = 2 * cosh(w/2 * ln(z))
```

```
e^(-w/2 * ln(z)) - e^(w/2 * ln(z)) = 2 * sinh(w/2 * ln(z))
```

```
exp(hau(z, w, w/2)) = z^(-w/2)
```

it's supersymmetry value
```
h(2, 4) = -ln(4) = ln(1/4) = -2 * ln(2)
```

ζ((z^2) ^ (1/2)) + c (c = h(2, 4) = -ln(4))
<img src="https://raw.githubusercontent.com/asyncker/fractals/refs/heads/main/render/zeta_abs.png">

ζ((z^2) ^ (1/2)) + c (c = h(2, 4) = -ln(4))
<img src="https://asyncker.github.io/fractals/render/zeta_abs_zoom.png">

Like quasicrystal with fractal:
```
τ(|Re(w)| + |Im(w)| * i, 1/2)
```

1 - exp(1/2 - (|Re(z)| + |Im(z)| * i))
<img src="https://asyncker.github.io/fractals/render/t((w%5E2)%5E(0.5)%2C0.5).png">

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

zeta function if use gamma:
```
zeta(z) =  ((2pi)^z / (gamma(z/2) * gamma(1 - z/2))) * gamma(1 - z) * zeta(1 - z)
```

```
sin(z * pi/2) * 2
amplitude: +2, -2
inter: ...-2, +2, −2,    +2, -2, +2...
zeros: ...-6, -4, -2, 0, +2, +4, +6...
```

invert function:
```
1 - z̄ = -z̄ + 1
1 - z = -z + 1
```

</br> Relu-curve ai:

define relumax, relumin:
```
relumax(x) = max(x, 0)
y1 = +relumax(log(x^3 - 2x + 2))
y2 = -relumax(log(x^3 - 2x + 2))
```

```
relumin(x) = min(x, 0)
y1 = +relumin(log(x^3 - 2x + 2))
y2 = -relumin(log(x^3 - 2x + 2))
```

```
relumax(z) + relumin(z) = ?
relumax(z) - relumin(z) = ?
relumin(z) + relumax(z) = ?
relumin(z) - relumax(z) = ?
```

<br/>

<br/>Any function can be given its re and im parts.<br/>
<br/>The re-part is the function's growth rate.<br/>
<br/>The im-part is the wave function.<br/>
<br/>A function can be given its cosine (re) and sinus (im) decompositions.
```
re(gamma(x + 1i)) it's cos-grow
im(gamma(x + 1i)) it's sin-grow
re(gamma(1 + xi)) it's cos-wave
im(gamma(1 + xi)) it's sin-wave
```

define gammasi:
```
gammasi(z) = 1 - gamma(1-z) / gamma(z)
```

gammasi on 1/2 im zeros:
```
2.7485719473580194676830788732357662506292818994028
4.0333153582981814452504488473440720760236022001631
5.0685937673417227119178328090976950022347182465278
5.9864659461340835531214031363237870149145455600539
6.831428663483892581910160812239621269992859042729
7.6251207322672948324163002511737145602880231561
8.3800571163918638811931313439848759778162314002634
9.1042716739771988147694564458892336322436421676236
9.8032975098107268252776305892834179176697704762788
10.481144228318346691429914578119016902528808583795
11.140831659447404065131548120407593031079474752449
11.784704109272636035773063739192536192868486203195
12.414626467252289142563245133276343088427451073617
13.032112404083050766257440638610631233204588756499
13.638411421526101291200718153301338744580110893572
14.234569864526178756209850613245307452295837257249
14.821474847389860535748106724071228268830259750719
15.39988661611396480058956408477347777521453048527
15.97046287294543680003499361046945361689371767039
16.533777382929145404971831702317007768520764272753
```

gammasi on 1/2 re zeros:
```
2.149767972757044487790458689919357792646779651259
3.314578364469234397953999338334297571359771837915
4.6410998632577700493412071426244967094710298687196
5.4849802116136612548550504229360476582946386556296
6.4581080721275214690838345912792449529389797653481
7.1985308993669859026377279364916644399564584231959
8.0367949020434448836859838226709648760134205841341
8.7191070880814617731525848364142979234735877645701
9.4801506223158208445991718441352929357038649675801
10.123306446958355513016872284257475365755180332373
10.832500441325213096563119802357684510622073676629
11.44668744012733391618976709168061198560313347638
12.117866727770881844096733476121086559824220603287
12.709356982981563083158621844564580484518028524851
13.351055302426493080256470007442080641569364332929
13.924057595030939865326005736718597572972466075821
14.541982980473780491122929897776325559162805114317
15.099495547210964222342991084700884362589658161808
15.697692206127357477759196043378950636930065150003
16.241947079737530036762580714713980547544356247169
```

define pgamma, gammapsi
```math
\frac{1}{\Gammaₚ(z)} = z e^{\gamma z} \prod_{p} \left( 1 + \frac{z}{p} \right) e^{-z/p}
```

```math
\frac{1}{\zeta(z)} = \prod_{p} 1 - p^{-s}
```

```
pgamma(z) = Γₚ(z)
```

```
gammapsi(z) = 1 - pgamma(1-z) / pgamma(z)
```

Hypothesis: all zeros of the gammapsi(z) with Re(z) > 0 and Re(z) < 1 lie on the critical line Re(z) = 1/2

If Re(z) >= 1 infinity zeros and Re(z) <= 0 infinity zeros

im(gammapsi(1/2 + ik)) zeros:
```
1.0293, 5.5865, 9.13, 11.79, 14.13, 16.29, 18.34, 20.29, 22.18, 24.01, 25.89, 27.55, 29.26, 30.95, 32.61, 34.24, 35.86, 37.45, 39.03, 40.6
```

re(gammapsi(1/2 + ik)) zeros:
```
8.25, 10.00, 13.38, 14.88, 17.64, 19.03, 21.51, 22.84, 25.15, 26.44, 28.63, 29.89, 31.99, 33.22, 35.25, 36.46, 38.44, 39.63, 41.55, 42.73
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

It's convenient to do something like this
```
F(f1, f2, f3, z) =  f3(f1'(z), f2(f1(z)))
F(gamma(z), /, *) = gamma'(z) * (1/gamma(z))
F(gamma(z), -, +) = gamma'(z) + (-1*gamma(z))
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

eps - exp(ln(eps)) = 0
w - exp(ln(w)) = 0

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
<img src="https://asyncker.github.io/fractals/render/scale_plane_algebra.png">
