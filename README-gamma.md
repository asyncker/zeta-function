```math
\chi(z) = \frac{\zeta(z)}{\zeta(1 - z)} = \frac{\Gamma\!\left(\tfrac{1 - z}{2}\right)}{\Gamma\!\left(\tfrac{z}{2}\right)} \cdot \pi^{z - 1/2}
```

Hypothesis: all zeros of the $f(z) = 1 - \chi(z)$ with 0 < Re(z) < 1 lie on the line Re(z) = 1/2

zeros at z = 1/2 + it, t ∈ R:

$$
t \in \{3.4362182, 9.6669081, 17.8455995, 23.1702827, 27.6701822, 31.7179800, 35.4671843, 38.9992100, 42.3635504, 45.5930290, 48.7107766, 51.7338428, 54.6752374, 57.5451652, 60.3518120, 63.1018680, \dots\}
$$

Weierstrass gamma function by primes:

```math
\frac{1}{Gp(z)} = z \prod_{p}^{\infty} \left( 1 + \frac{z}{p} \right) e^{-z/p}
```

Note: The integral converges absolutely for $z \in \mathbb{C} \setminus (-\infty, -2]$

```math
\frac{1}{Gp(z)} = {z} \exp\left( - \int_{2}^{\infty} \pi(x) \frac{z^2}{x^2(x+z)} \, dx \right)
```

```math
\Phi(z) = \dfrac{Gp\left(\frac{1 - z}{2}\right)}{Gp\left(\frac{z}{2}\right)}
```

Hypothesis: all zeros of the $f(z) = 1 - \Phi(z)$ with 0 < Re(z) < 1 lie on the line Re(z) = 1/2

zeros at z = 1/2 + it, t ∈ R:

$$
t \in \{7.5593242, 14.6100647, 20.3194037, 25.5268164, 30.4450039, 35.1672954, 39.7447722, 44.2091084, 48.5815992, 52.8774028, 57.1077783, 61.2813706, 65.4049958, 69.4841471, 73.5233328, 77.5263103, \dots\}
$$

References:
1. Fröberg, C. E. (1968). On the prime zeta function. BIT Numerical Mathematics, 8(3), 187–202.
2. Apostol, T. M. (1976). Introduction to Analytic Number Theory. Springer-Verlag.
