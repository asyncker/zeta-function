zsinh(z, t) = (ζ(t + z) - ζ(t - z)) / 2
zcosh(z, t) = (ζ(t + z) + ζ(t - z)) / 2
ζ(t + z) = zcosh(z, t) + zsinh(z, t)
ζ(t + z) * ζ(t - z) = zcosh(z, t)^2 - zsinh(z, t)^2

Нули zsinh и zcosh чередуется при t<1/2 как только t=1/2 чередование нарушается. arg(ζ(it)), её производная ~= -ln(t/2pi) и логарифм подавляет флуктуации при больших t.
zsinh_zeros[i] < zcosh_zeros[i] (все истина кроме первого при t<1/2)

Пример чередование нулей zsinh и zcosh при (t = 1/2 - 0.00001): [3.43621400, 0.81955124, 9.66691026, 14.13466233, 14.13472673, 14.51798335, 17.84559970, 20.65399921, 21.02203739, 21.02208423, 23.17028211, 25.01082878, 25.01086105, 25.49153867, 27.67018256, 29.73849079 ...]

Фракталы от zeta функции:
ζ(z) + 0 (https://asyncker.github.io/fractals/render/pic17.png)
ζ(|Re(z)| + |Im(z)| * i) + 0 (https://asyncker.github.io/fractals/render/pic21.png)
ζ(|Re(z)| + |Im(z)| * i) + 1/(-0.724775731 + 0i) (https://asyncker.github.io/fractals/render/zeta-inv-conj-burning-ship-0.724775731.png)
ζ(z) + c (https://asyncker.github.io/fractals/render/zeta-mandelbrot-zoom.png)
zcosh(z, 1/2) + c (https://asyncker.github.io/fractals/render/zcosh-mandelbrot-zoom.png)
zsinh(z, 1/2) + c (https://asyncker.github.io/fractals/render/zsinh-mandelbrot-zoom.png)
ln(sin(1 / (|Re(z)| + |Im(z)| * i))) + c (c ~= -0.4670670970289143 + 0.008333333333333333i) (https://asyncker.github.io/fractals/render/log_sin_test.png)
zeta(z ^ 0.27) + 0 (https://asyncker.github.io/fractals/render/zeta_pow.png)
exp(z ^ 0.27) + 0 (https://asyncker.github.io/fractals/render/exp_pow.png)

Im(ζ(iz + 1/2) * ζ(-iz + 1/2)) можно создать общую функцию харди Z(x, t) и взять t = 1/2 (это оригинальная функция) и t = -1/2 и получится через Im и Re тоже самое

zeta сложно сделать через quaternion, но легко в 4d через bicomplex, используя идемпотентность. Также отобразить zeta в гильбертовом простнатсве/эрмитовы операторы является задачей где я копаю. Ещё нужны мультипликативные интегралы и производны не-ньютоновские исчисления. И многозначные функции arcgamma

Идея создать алгебру, которая включает/объединяет элементы: p-adic, неархмедовых, гиперреальных, многочлены Лорана, кольцо Лорана. Всё начинается с +-*/^root (положительные, отрицательные, дробные числа, -, иррациональные, комплексные) и прочерк закроют новые числа:
ω^-1 = ε
ε^-1 = ω
+∞ > ω > 10^1000000
+0 < ε < 10^-1000000
ω и ε отображают маштаб (ω^-7 * 6.246) вот плоскость https://asyncker.github.io/fractals/render/scale_plane_algebra.png
0.999999... * ω = ...999999.0 и 1 * ω = ω теперь пробел не 0 и ε, а 0 и 1 выходит между 0.999999... и 1 несчётно много чисел 
(ω - 1) * 1/ω = 1 - ε (ω являются решением этого уравнения (x - 1) * 1/x = 0.999999...)

Можно вписывать примерные значения ε ~= 0.001 и ω ~= 1000, прикладной смысл в программирование, физики и тд:
ln(ε) = -ln(ω)
ln(ω) = -ln(ε)
ln(ω^ε) = -ε * ln(ε)
ε * ω = 1
15 * ω^3 * ε^2 + 3 * ω = 18ω
nround(+ε) = +0
around(-∞) = -ω
