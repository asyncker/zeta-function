```math
\chi(z) = \frac{\zeta(z)}{\zeta(1 - z)} = \frac{\Gamma\!\left(\tfrac{1 - z}{2}\right)}{\Gamma\!\left(\tfrac{z}{2}\right)} \cdot \pi^{z - 1/2}
```

Hypothesis: all zeros of the 1 - χ(z) with Re(z) > 0 and Re(z) < 1 lie on the critical line Re(z) = 1/2

```
f(z) = 1 - χ(z)
z = 1/2 + it, t ∈ R zeros at t={3.4362182, 9.6669081, 17.8455995, 23.1702827, 27.6701822, 31.7179800, 35.4671843, 38.9992100, 42.3635504, 45.5930290, 48.7107766, 51.7338428, 54.6752374, 57.5451652, 60.3518120, 63.1018680...}
```

Weierstrass gamma function by primes and replace γ to 0

```math
\frac{1}{Gp(z)} = z \prod_{p}^{\infty} \left( 1 + \frac{z}{p} \right) e^{-z/p}
```

```math
\frac{1}{Gp(z)} = {z} \exp\left( - \int_{2}^{\infty} \pi(x) \frac{z^2}{x^2(x+z)} \, dx \right)
```

Hypothesis: all zeros of the 1 - Gp((1 - z) / 2) / Gp(z / 2) with Re(z) > 0 and Re(z) < 1 lie on the critical line Re(z) = 1/2
```
f(z) = 1 - Γ((1 - z) / 2) / Γ(z / 2)
z = 1/2 + it, t ∈ R zeros at t={6.1680546, 10.5921764, 14.0544503, 17.1172819, 19.9410492, 22.5995625, 25.1343279, 27.5715454, 29.9290628, 32.2197156, 34.4531187, 36.6367064, 38.7763749, 40.8768989, 42.9422132, 44.9756082...}

f(z) = 1 - Gp((1 - z) / 2) / Gp(z / 2)
z = 1/2 + it, t ∈ R zeros at t={7.5593242, 14.6100647, 20.3194037, 25.5268164, 30.4450039, 35.1672954, 39.7447722, 44.2091084, 48.5815992, 52.8774028, 57.1077783, 61.2813706, 65.4049958, 69.4841471, 73.5233328, 77.5263103...}
```
