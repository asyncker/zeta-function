```math
\frac{1}{1 - 2^{1 - z}} = \frac{\zeta(z)}{\eta(z)}
```

```math
\frac{1}{1 - e^{1 - z}}
```

```math
1 - e^{\frac{1}{2} - z}
```

Bose-Einstein (-1):
```math
\frac{(1 - e^{t - z})'}{(1 - e^{t - z})} = \frac{+1}{e^{z - t} - 1}
```

Fermi-Dirac (+1):
```math
\frac{(1 + e^{t - z})'}{(1 + e^{t - z})} = \frac{-1}{e^{z - t} + 1}
```

Maxwell–Boltzmann (-0)
```math
\frac{\partial_t e^{t - z}}{e^{t - z}} = +1
```

Maxwell–Boltzmann (+0)
```math
\frac{\partial_z e^{t - z}}{e^{t - z}} = -1
```

<table>
  <tr>
    <td><img src="https://asyncker.github.io/zeta-function/img/1-exp(0.5-z).png" alt="1 - exp(1/2 - z)"></td>
    <td><img src="https://asyncker.github.io/zeta-function/img/zeta(z).png" alt="zeta(z)"></td>
  </tr>
  <tr>
    <td align="center"><code>1 - exp(1/2 - z)</code></td>
    <td align="center"><code>zeta(z)</code></td>
  </tr>
</table>

```math
h(z, w) = -\frac{w}{2}\,\ln(z)
```

```math
\frac{\partial_z\, h(z, w)}{h(z, w)} = \frac{1}{z \ln(z)}
```

```math
h(2, 4) = -2\ln 2 = -\ln 4
```

Symetric reflection:

```math
\pm z = \sqrt{z^2},\quad |z| = \sqrt{z\bar z},\quad |\Re(z)| + |\Im(z)|\,i
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

```math
\chi(z) = \frac{\zeta(z)}{\zeta(1 - z)} = \frac{\Gamma\!\left(\tfrac{1}{2} - \tfrac{z}{2}\right)}{\Gamma\!\left(\tfrac{z}{2}\right)} \cdot \pi^{z - 1/2}
```

```math
\eta(z) = \frac{1 - 2^{1 - z}}{1 - 2^{z}} \cdot \chi(z) \cdot \eta(1 - z)
```

```math
\zeta(z) = \frac{\eta(z)}{1 - 2^{\,1 - z}}
```

Conjecture: all zeros of the 1 - χ(z) with 0 < Re(z) < 1 lie on the critical line Re(z) = 1/2
```
Let z = 1/2 + it, t ∈ R zeros at t={3.4362182, 9.6669081, 17.8455995, 23.1702827, 27.6701822, 31.7179800, 35.4671843, 38.9992100, 42.3635504, 45.5930290, 48.7107766, 51.7338428, 54.6752374, 57.5451652, 60.3518120, 63.1018680}
```

```math
\frac{1}{\zeta(z)} = \prod_{p}^{\infty} 1 - p^{-z}
```

```math
\frac{\zeta(z)}{\zeta(1 - z)} = \prod_{p}^{\infty} \frac{1-p^{z-1}}{1-p^{-z}}
```

```math
\frac{1}{G_p(z)} = z \prod_{p}^{\infty} \left( 1 + \frac{z}{p} \right) e^{-z/p}
```

```math
\frac{1}{G_p(z)} = {z} \exp\left( - \int_{2}^{\infty} \pi(x) \frac{z^2}{x^2(x+z)} \, dx \right)
```

```math
\mathrm{psinh}(z) = {z} \prod_{p}^{\infty} \left(1 + \frac{z^{2}}{\pi^{2} p^{2}}\right)
```

```math
\boxed{
\frac{G_p\!\left(\tfrac12-\tfrac z2\right)}{G_p\!\left(\tfrac z2\right)} = \frac{z}{1-z}\prod_{p}\left[\frac{p+\tfrac z2}{p+\tfrac{1-z}{2}}\,e^{-\frac{z-1/2}{p}}\right]
}
```

```math
\boxed{\frac{G_p'(z)}{G_p(z)} = -\frac{1}{z} + \sum_p \left[\frac{1}{p} - \frac{1}{p+z}\right] = -\frac{1}{z} + z\sum_p \frac{1}{p(p+z)}}
```

Conjecture: all zeros of the 1 - Gₚ(1/2 - z/2) / Gₚ(z/2) with 0 < Re(z) < 1 lie on the line Re(z) = 1/2
```
Let z = 1/2 + it, t ∈ R zeros at t={7.5593242, 14.6100647, 20.3194037, 25.5268164, 30.4450039, 35.1672954, 39.7447722, 44.2091084, 48.5815992, 52.8774028, 57.1077783, 61.2813706, 65.4049958, 69.4841471, 73.5233328, 77.5263103...}
```

Conjecture: infinity zeros of the 1 - Gₚ(t - z/2) / Gₚ(z/2) lie on the line Re(z) = t

Conjecture: infinity zeros of the Gₚ(t - z/2) - Gₚ(z/2) lie on the line Re(z) = t

Truncate method:

Simplifying the problem by taking not an infinite sum/product, but a finite one, and it should still converge and give symmetry

```math
\frac{1}{f_p(z)} = z \prod_{p}^{3} \left( 1 + \frac{z}{p} \right) e^{-z/p}
```

```math
\Phi(z) = 1 - \frac{f_p(\frac{1}{2} - \frac{z}{2})}{f_p(\frac{z}{2})} = 1 - \frac{(1 - z) \cdot (5 - z) \cdot (7 - z)}{(0 + z) \cdot (4 + z) \cdot (6 + z)} \cdot exp(\frac{5 \cdot (2z - 1)}{12})
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

Conjecture:
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

Add asymptotic and count function ptlim. ptlim - test to see if a number is prime as n approaches +∞ and at what n this ends.
```math
\text{ptlim}(f) = \{ n \in \mathbb{Z}_{\ge 0} \mid f(n) \in \mathbb{P} \}, \mathbb{P} = \{2, 3, 5, 7, 11, 13, \dots\}
```

```math
\text{count}(s) = \left( \big| \{ k \in s \mid k \le n \} \big| \right)_{n=0}^{\infty}
```

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
ptlim(12 \cdot (2^n - 1) - 1) = \{1, 3, 4, 7, 9, 12, 15, 16, 25, 37, 40, 43, 49, 72, 75, 124, 180, 196, 208, 312, 480, 568, 1113, 1729...\}
```

```math
ptlim(2^n \cdot 33 - 65) = \{2, 3, 4, 5, 7, 9, 13, 15, 16, 18, 19, 20, 21, 23, 26, 27, 37, 40, 43, 45, 46, 53, 55, 56, 58, 59, 62, 64, 69, 79, 81, 85, 98, 106, 146, 154, 173, 179, 197, 289, 331, 359, 602, 612, 615, 657, 675, 823, 885, 901, 931, 988, 1033, 1039, 1089, 2313, 2671, 3066, 3203, 3813, 4735, 4786, 5114, 5384, 5823, 5832, 6610, 6817, 7800, 10432, 13009, 14802, 18577, 18841, 20612, 23037, 23877, 25673, 27951, 34276, 35656, 36358, 38224...\}
```

```math
\mathrm{count}(\mathrm{ptlim}(n)) = \pi(n) = \{0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7,\dots\}
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
ptlim(n) \sim \lceil x \cdot (\ln(x) + \ln(\ln(x)) - 1)\rceil
```

if take exp for prime asymtotic this get special gamma function encoding prime number
```math
exp(z \cdot (\ln(z) + \ln(\ln(z)) - 1)) = z^z \cdot \ln(z)^z \cdot exp(-z)
```

Set coordinate by initial numbers: (naturals, fibonacci, squares, prime, random and etc.). Add ℤ, ℚ, 𝕀, ℂ between sequence
```math
n_p = \{ - \infty \dots, -11, -7, -5, -3, -2, \pm 0, +2, +3, +5, +7, +11, \dots + \infty \}
```

```math
\Re(x_p) = (1 - t)\,n_k + t\,n_{k+1}, \quad t = \frac{x - n_k}{n_{k+1} - n_k}
```

```math
\Im(x_p) = \Re(x_p)
```

```math
z_p = \Re(x_p) + i\,\Im(x_p)
```

if use coordinate by prime you get automatic naturals to primes:
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
\sum_{p}^{\infty} 2^{-p} = 0.4146825...
```

```math
\sum_{p}^{\infty} p^{-2} = 0.4522474...
```

```math
f(s) = \sum_{p}^{\infty} s^{-p}
```

```math
P(s) = \sum_{p}^{\infty} p^{-s}
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
(1 + \varepsilon)^{\frac{\ln(2)}{\ln(1 + \varepsilon)}} = 2
```

```math
(1 + \varepsilon)^{2} = 1 + (2\varepsilon + \varepsilon^{2})
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
