# Zeta Based Functions

Fractals of the zeta: https://asyncker.github.io/zeta-function/zeta_fractal.html

```math
f(z)^{-} = 1 - f(z)
```

```math
f(z)^{+} = 1 + f(z)
```

```math
\mathrm{fau}(f, z, t, v, a) = ({f(t \cdot 2v - z \cdot v)} / {f(z \cdot v)}) \cdot a
```

```math
\mathrm{fis}(f, z, t, v, a) = ({f(t \cdot 2v - z \cdot v)} - {f(z \cdot v)}) \cdot a
```

```math
\mathrm{fic}(f, z, t, v, a) = ({f(t \cdot 2v - z \cdot v)} + {f(z \cdot v)}) \cdot a
```

```
v = freq (default = 1/2 or 1)
t = shift (default = 1/2 or 0)
a = amp (default = 1/2 or 1)
x = base-power function (default = e or pi)
z = exponent-power function (default = z)
```

```math
tau(z, t, v) = \frac{x^{t \cdot 2v - z \cdot v}}{x^{z \cdot v}} = x^{t \cdot 2v - z \cdot 2v}
```

```math
\mathrm{gau}(z, t, v) = \frac{\Gamma(t \cdot 2v - z \cdot v)}{\Gamma(z \cdot v)}
```

```math
\tau_x(z, t) = x^{t - z}
```

```math
g(z, t) = \frac{\Gamma(t - \frac{z}{2})}{\Gamma(\frac{z}{2})}
```

Bose-Einstein (-1) and Fermi-Dirac (+1):
```math
\frac{\tau'(z, t)^{-}}{\tau(z, t)^{-}} = \frac{+1}{e^{z - t} - 1}
```

```math
\frac{\tau'(z, t)^{+}}{\tau(z, t)^{+}} = \frac{-1}{e^{z - t} + 1}
```

Maxwell–Boltzmann (-0) and Maxwell–Boltzmann (+0):
```math
\frac{\partial_t \tau(z, t)}{\tau(z, t)} = +1
```

```math
\frac{\partial_z \tau(z, t)}{\tau(z, t)} = -1
```

The zeros lie on Re(z) = 1/2 for any x > 0 except x = +1
```math
\tau_x(z, \frac{1}{2})^{-} = 1 - x^{\frac{1}{2} - z}
```

```math
\tau_x(z, \frac{1}{2})^{+} = 1 + x^{\frac{1}{2} - z}
```

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

```math
\tau'(z, t)^{-} + \tau(z, t)^{-} = 1
```

```math
\tau(z, \frac{1}{2})^{-} - \tau(1 - z, \frac{1}{2})^{-} = 0 + 2 \cdot sinh(z - \frac{1}{2})
```

```math
\tau(z, \frac{1}{2})^{-} + \tau(1 - z, \frac{1}{2})^{-} = 2 - 2 \cdot cosh(z - \frac{1}{2})
```

```math
\tau(z, \frac{1}{2})^{-} \cdot \tau(-z, \frac{1}{2})⁻ = 1 + e - \sqrt e \cdot 2 \cdot cosh(z)
```

```math
\tau(iθ, \frac{1}{2})^{-} \cdot \tau(−iθ, \frac{1}{2})^{-} = (1 - sqrt(e))^{2} + 4 \cdot sqrt(e) \cdot sin(θ/2)^{2}
```

```math
z^{-w/2} - z^{w/2} = -2 \cdot sinh(\frac{w}{2} \cdot \ln(z))
```

```math
z^{-w/2} + z^{w/2} = +2 \cdot cosh(\frac{w}{2} \cdot \ln(z))
```

```math
\frac{g'(z, t)}{g(z, t)} = \psi(t - \frac{z}{2})
```

```math
\frac{\left(e^{z-t} - 1\right)'}{e^{z-t} - 1} = \frac{1}{1 - e^{t-z}} = \frac{e^{z-t}}{e^{z-t} - 1}
```

```math
f(z, u, t) = u / (t * z^{2}) * (e^{u / (z * t)} / (e^{u / (z * t)} - 1))
```

```math
hau(z, w, t, v) = (t \cdot 2v - w \cdot v) \cdot \ln(z)
```

```math
h(z, w) = -\frac{w}{2}\,\ln(z) = \mathrm{hau}\!\left(z,\, w,\, \frac{w}{2},\, \frac{1}{2}\right)
```

```math
h(z, w) + h(z, -w) = 0
```

```math
\partial_z\, h(z, w) = -\frac{w}{2z}
```

```math
\partial_w\, h(z, w) = -\frac{1}{2}\,\ln(z)
```

```math
\frac{\partial_z\, h(z, w)}{h(z, w)} = \frac{1}{z \ln(z)}
```

```math
sin(z \cdot \frac{\pi}{2}) \cdot 2i = (1 - (-1)^{-z/2}) - (1 - (-1)^{z/2})
```

```math
sin(z \cdot \frac{\pi}{2}) \cdot 2 = -i \cdot ((-1)^{z/2} - (-1)^{-z/2})
```

```math
1 - (-1)^{-z}
```

```math
h(2, 4) = -\ln 4 = \ln \frac{1}{4} = -2\ln 2
```

Fractal zeta and exp function:

```math
z_{n+1} = \zeta\!\left(\sqrt{z_n^2}\right) - \ln 4
```
<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/asyncker/fractals/refs/heads/main/render/zeta_abs.png"></td>
    <td><img src="https://asyncker.github.io/fractals/render/zeta_abs_zoom.png"></td>
  </tr>
  <tr>
    <td align="center"><code>ζ(±z) - ln(4)</code></td>
    <td align="center"><code>ζ(±z) - ln(4)</code></td>
  </tr>
</table>

<table>
  <tr>
    <td><img src="https://github.com/asyncker/fractals/blob/main/render/abszeta(1-z)-1.png" alt="zeta(|Re(z)| + |Im(z)|*i + 1) - 1"></td>
    <td><img src="https://github.com/asyncker/fractals/blob/main/render/abs1div(exp(z)-1).png" alt="1/(exp(|Re(z)| + |Im(z)|*i) - 1))"></td>
  </tr>
  <tr>
    <td align="center"><code>ζ(±z + 1) - 1</code></td>
    <td align="center"><code>1 / (exp(±z) - 1)‎</code></td>
  </tr>
</table>

<table>
  <tr>
    <td><img src="https://asyncker.github.io/fractals/render/t((w%5E2)%5E(0.5)%2C0.5).png"></td>
  </tr>
  <tr>
    <td align="center"><code>1 - exp(1/2 - ±z)</code></td>
  </tr>
</table>

```math
\zeta(\pm z) - c, \qquad c \in \left\{\, 2\ln 2,\ \sqrt{2},\ 2,\ 2 \pm \varepsilon,\ \tfrac{1}{2},\ \tfrac{e}{2},\ \tfrac{\pi}{2} \,\right\}
```

```math
\chi(z) = \frac{\zeta(z)}{\zeta(1 - z)} = \frac{\Gamma\!\left(\tfrac{1}{2} - \tfrac{z}{2}\right)}{\Gamma\!\left(\tfrac{z}{2}\right)} \cdot \pi^{-1/2 + z}
```

```math
\chi(z) = (2\pi)^{z-1} \cdot 2 \cdot \sin\!\left(\frac{z\pi}{2}\right) \Gamma(1-z)
```

```math
\frac{1}{\chi(z)} = \frac{\zeta(1 - z)}{\zeta(z)}
```

```math
\eta(z) = \frac{1 - 2^{1 - z}}{1 - 2^{z}} \cdot \chi(z) \cdot \eta(1 - z)
```

```math
\zeta(z) = \frac{\eta(z)}{1 - 2^{\,1 - z}}
```

Hypothesis: all zeros of the 1 - ζ(z) / ζ(1 - z) with Re(z) > 0 and Re(z) < 1 lie on the critical line Re(z) = 1/2

```
f(z) = gamma(1/2 - z/2) / gamma(z/2) * pi^(-1/2 + z)
zeros: {3.4362182, 9.6669081, 17.8455995, 23.1702827, 27.6701822, 31.7179800, 35.4671843, 38.9992100, 42.3635504, 45.5930290, 48.7107766, 51.7338428, 54.6752374, 57.5451652, 60.3518120, 63.1018680}
```

```math
\tau_2(z, 1)^{-} = 1 - 2^{\,1 - z}
```

```math
\tau_p(z, 0)^{-} = 1 - p^{-z}
```

```math
\frac{1}{\zeta(z)} = \prod_{p} 1 - p^{-z}
```

```math
\frac{\zeta(z)}{\zeta(2z)} = \prod_{p} 1 + p^{-z}
```

```math
\frac{1}{G_p(z)} = z \prod_{p} \left( 1 + \frac{z}{p} \right) e^{-z/p}
```

```math
\frac{1}{G_p(z)} = {z} \exp\left( - \int_{2}^{\infty} \pi(x) \frac{z^2}{x^2(x+z)} \, dx \right)
```

Hypothesis: all zeros of the 1 - Gₚ(1/2 - z/2) / Gₚ(z/2) with Re(z) > 0 and Re(z) < 1 lie on the critical line Re(z) = 1/2
```
f(z) = 1 - Γ(1/2 - z/2) / Γ(z/2)
zeros: {6.1680546, 10.5921764, 14.0544503, 17.1172819, 19.9410492, 22.5995625, 25.1343279, 27.5715454, 29.9290628, 32.2197156, 34.4531187, 36.6367064, 38.7763749, 40.8768989, 42.9422132, 44.9756082...}

f(z) = 1 - Gₚ(1/2 - z/2) / Gₚ(z/2)
zeros: {7.5593242, 14.6100647, 20.3194037, 25.5268164, 30.4450039, 35.1672954, 39.7447722, 44.2091084, 48.5815992, 52.8774028, 57.1077783, 61.2813706, 65.4049958, 69.4841471, 73.5233328, 77.5263103...}
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

Symmetric formulas:

```math
S(z) = \frac{f(z) - f(-z)}{2}
```

```math
U(z) = \frac{f(z)}{f(-z)}
```

```math
F(z) = \frac{f'(z)}{f(z)}
```

```math
S'(z) = \frac{f'(z) + f'(-z)}{2}
```

```math
F'(z) = \frac{f''(z)}{f(z)} - F(z)^{2}
```

```math
U'(z) = (F(z) + F(-z)) \cdot U(z)
```

Function by component:

```math
\min.\left(\max.\left(\,\zeta(z),\, -\frac{1}{\varepsilon}\right),\, \frac{1}{\varepsilon}\right) \approx \mathrm{Re}\,\zeta(z)
```

```math
\min.\left(\max.\left(\,-i \cdot \zeta(z),\, -\frac{1}{\varepsilon}\right),\, \frac{1}{\varepsilon}\right) \approx \mathrm{Im}\,\zeta(z)
```

```math
\max.(z, 0) + \min.(z, 0) = z
```

```math
\max.(z, 0) - \min.(z, 0) = +|\mathrm{Re}(z)| + |\mathrm{Im}(z)|\, i
```

```math
\min.(z, 0) - \max.(z, 0) = -|\mathrm{Re}(z)| - |\mathrm{Im}(z)|\, i
```

```math
y = \pm\max(\ln\left(x^{3} - 2x + 2\right),\, 0)
```

Empty ◇ means there is no function value at this point. All functions except the equal sign (=) are prohibited, and ◇ is not equal to anything except itself. x = ◇ like float x; in programming language without value.
```math
\mathrm{relumaxU}(z) = \begin{cases} z, & z \ge +0 \\ \diamond, & z < +0 \end{cases}
```

```math
\mathrm{reluminU}(z) = \begin{cases} z, & z \le -0 \\ \diamond, & z > -0 \end{cases}
```

```math
mpow(z, w) = |z|^w \cdot \exp\!\left(i \cdot \arg(z) \cdot \frac{1 - (-1)^w}{2}\right), \quad w \in \mathbb{N}
```

```math
fol(z, w) = \sqrt[w]{z^w}
```

```math
dot(z, w) = z \cdot \bar{w}
```

```math
abs(z, w) = \sqrt{z \cdot \bar{w}}
```

```math
phs(z, w) = \sqrt{z / \bar{w}}
```

```math
dos(z, w, k, t) = \left(z \cdot \left(\bar{w}\right)^t\right)^k
```

```math
non(z, w) = \frac{\ln(w / z)}{w} \cdot i
```

```math
non'(z, w) = -\frac{i}{z \, w}
```

zeta bicomplex 4d with idempotent
```math
\mathrm{BL}(z) = (z_x - z_w) + (z_y + z_z)\, i
```

```math
\mathrm{BR}(z) = (z_x + z_w) + (z_y - z_z)\, i
```

```math
\mathrm{BW}(z, w) = \frac{1}{2}\left(w_x + z_x,\; z_y + w_y,\; z_y - w_y,\; w_x - z_x\right)
```

```math
\mathrm{bizeta}(z) = BW(\zeta(BL(z)), \zeta(BR(z)))
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

```math
\Phi_6(z, w) = z^{2w} - z^{1w} + 1 = 1 + (z^w - 1) * z^w
```

```math
\Phi_6(10, 2) = 9901
```

```math
\Phi_6(10, 4) = 99990001
```

```math
\Phi_6(10, 6) = 999999000001
```

```math
\Phi_6(10, 8) = 9999999900000001
```

```math
33333333333333336666666666666667 = 7 \cdot 13 \cdot 37 \cdot 9901 \cdot 99990001 \cdot 9999999900000001
```

Add asymptotic and count function ptlim. ptlim - test to see if a number is prime as n approaches +∞ and at what n this ends.
```math
ptlim(10^n) = ∅
```

```math
ptlim(10^{2n} - 10^{n} + 1) = \{2, 4, 6, 8\}
```

```math
ptlim(2n + 1) = \{1, 2, 3, 5, 6, 8, 9, 11, 14, 15, 18, 20...\}
```

```math
ptlim(10^n + 7) = \{1, 2, 4, 8, 9, 24, 60, 110, 134, 222, 412, 700, 999...\}
```

```math
ptlim(2^n \cdot 3 - 1) = \{0, 1, 2, 3, 4, 6, 7, 11, 18, 34, 38, 43, 55, 64, 76, 94, 103, 143, 206, 216, 306, 324, 391, 458, 470, 827...\}
```

```math
ptlim(2^n \cdot 14388 - 12545) = \{1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 20, 29, 31, 34, 35, 41, 43, 50, 61, 74, 79, 82, 83, 89, 97...\}
```

```math
ptlim(2^n \cdot 33 - 65) = \{2, 3, 4, 5, 7, 9, 13, 15, 16, 18, 19, 20, 21, 23, 26, 27, 37, 40, 43, 45, 46, 53, 55, 56, 58, 59, 62, 64, 69, 79, 81, 85, 98, 106, 146, 154, 173, 179, 197, 289, 331, 359, 602, 612, 615, 657, 675, 823, 885, 901, 931, 988, 1033, 1039, 1089, 2313, 2671, 3066, 3203, 3813, 4735, 4786, 5114, 5384, 5823, 5832, 6610, 6817, 7800, 10432, 13009, 14802, 18577, 18841, 20612, 23037, 23877, 25673, 27951, 34276, 35656, 36358, 38224...\}
```

```math
ptlim(12 \cdot (2^n - 1) - 1) = \{1, 3, 4, 7, 9, 12, 15, 16, 25, 37, 40, 43, 49, 72, 75, 124, 180, 196, 208, 312, 480, 568, 1113, 1729...\}
```

```math
\mathrm{count}(\mathrm{ptlim}(n)) = \pi(n) = \mathrm{count}(\{2,3,5,7,11,13,17,\dots\}) = \{0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7,\dots\}
```

```math
\mathrm{count}(\mathrm{ptlim}(n)) \sim \left\lceil \frac{x}{\ln(x) - 1} \right\rceil
```

```math
\mathrm{count}(\mathrm{ptlim}(2^n \cdot 33 - 65)) \sim \lfloor 7 \cdot \ln(x) \rfloor
```

```math
\mathrm{count}(\mathrm{ptlim}(2^n - 1)) \sim \lfloor 2 \cdot \ln(x) \rfloor
```

```math
a = 2^{n} \cdot 5^{m} \text{(all non-periodic fractions in the 10-adics)}
```

Any-adic set coordinate by initial numbers: (naturals, fibonacci, squares, prime, random and etc.). Add ℤ, ℚ, 𝕀, ℂ between sequence
```math
n_p = \{ - \infty \dots, -11, -7, -5, -3, -2, \pm 0, +2, +3, +5, +7, +11, \dots + \infty \}
```

```math
\mathrm{Re}(x_p) = (1 - t)\,n_k + t\,n_{k+1}, \quad t = \frac{x - n_k}{n_{k+1} - n_k}
```

```math
\mathrm{Im}(x_p) = \mathrm{Re}(x_p)
```

```math
z_p = \mathrm{Re}(x_p) + i\,\mathrm{Im}(x_p)
```

if use coordinate you get automatic naturals to primes:
```math
p - 1 = 1,\, 2,\, 4,\, 6,\, 10,\, 12,\, 16,\, 18,\, 22,\, \dots = z_{p} -1
```

```math
p \cdot 2 = 4,\, 6,\, 10,\, 14,\, 22,\, 26,\, 34,\, \dots = z_{p}\cdot2
```

```math
p^{2} = 4,\, 9,\, 25,\, 49,\, 121,\, 169,\, \dots = z_{p}^{2}
```

```math
2^{p} = 4,\, 8,\, 32,\, 128,\, 2048,\, 8192,\, 131072,\, \dots = 2^{z_{p}}
```

```math
p! = 2,\, 6,\, 120,\, 5040,\, 39916800,\, \dots = \Gamma(z_{p} + 1)
```

```math
p^{p} = 4,\, 27,\, 3125,\, 823543,\, 285311670611,\, \dots = z_{p}^{z_{p}}
```

```math
\sum_{p}^{\infty} \frac{1}{2^p} = 0.4146825...
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

family of gamma 1 / (z · e^wz · ∏ₛ((1 + z/n) · e^(−z/n))) (if x<0 switch sign {-1, +1} to {+1, -1} in prime, random, etc.), exp (2pi * prime, 2pi * random, etc.)
```math
\frac{1}{\Gamma(z, w, s = \{2,3,5,7...\})} = ze^{wz} \prod_{n \in s} \left(1 + \frac{z}{n}\right) e^{-z/n}
```

```math
\mathrm{sinh}(z, s = \{2,3,5,7...\}) = z \prod_{n=s} \left(1 + \frac{z^{2}}{\pi^{2} n^{2}}\right)
```

epsilon and omega numbers:
```math
\varepsilon^{-1} = \omega
```

```math
\omega^{-1} = \varepsilon
```

```math
\omega \cdot \varepsilon = 1
```

```math
\ln(\varepsilon) = -\ln(\omega)
```

```math
\ln(\omega) = -\ln(\varepsilon)
```

```math
\ln\!\left(\varepsilon^{\varepsilon}\right) = -\varepsilon \cdot \ln(\omega)
```

```math
\mathrm{sv}(x) = \{ f(x - \varepsilon), f(x + \varepsilon) \}
```

```math
\mathrm{signs}(x) = \{ \mathrm{sgn}(f(x - \varepsilon)), \mathrm{sgn}(f(x + \varepsilon)) \}
```

```math
sym(x) = \frac{|f(x - \varepsilon)| + |f(x + \varepsilon)|}{2}
```

```math
3 \cdot 0.333 + 0.001 = 1
```

Solve the equation using epsilone and omega

```math
(\omega - 1) \cdot \frac{1}{\omega} = 1 - \varepsilon
```

```math
(1 - \varepsilon) \cdot \frac{1}{\varepsilon} = \omega - 1
```

```math
(1 - \varepsilon) \cdot \omega + (\omega - 1) \cdot \varepsilon = \omega - \varepsilon
```

```math
(\omega - 1) \cdot \omega + 1 = \frac{1 - \varepsilon + \varepsilon^{2}}{\varepsilon^{2}}
```

```math
\left(\varepsilon^{2} + \varepsilon^{2}\right)^{k} = 2^{k} \cdot \varepsilon^{2k}
```

```math
sym(\Gamma(0)) \approx \left( \frac{1}{\varepsilon} + \varepsilon \right)
```

```math
signs(\Gamma(0)) = \{-, +\}
```

```math
signs(\Gamma(-1)) = \{+, -\}
```

Scale plane (x-axis it's mult coefficient for eps or w y-asis it's power (example x * eps^y)):<br />
<img src="https://asyncker.github.io/fractals/render/scale_plane_algebra.png">
