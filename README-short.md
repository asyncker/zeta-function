zsinh(z, t) = (ζ(t + z) - ζ(t - z)) / 2
zcosh(z, t) = (ζ(t + z) + ζ(t - z)) / 2

ζ(t + z) = zcosh(z, t) + zsinh(z, t)
ζ(t + z) * ζ(t - z) = zcosh(z, t)^2 - zsinh(z, t)^2

Если t<1/2 нули чередуются у zsinh(z, t), zcosh(z, t), при t=1/2 чередование нарушается. arg(ζ(it)), её производная ~= -ln(t/2π) и логарифм подавляет флуктуации при больших t
zsinh_zeros[i] < zcosh_zeros[i] (все истина кроме первого при t<1/2)

Чередование нулей zsinh, zcosh при t = 1/2 - 0.00001 [3.43621400, 0.81955124, 9.66691026, 14.13466233, 14.13472673, 14.51798335, 17.84559970, 20.65399921, 21.02203739, 21.02208423, 23.17028211, 25.01082878, 25.01086105, 25.49153867, 27.67018256, 29.73849079 ...]

Im(ζ(iz + 1/2) * ζ(-iz + 1/2)) можно создать общую функцию харди Z(x, t) и взять t = 1/2 (оригинальная функция), t = -1/2 и через Im и Re

Фракталы от zeta:
ζ(z) + 0 https://asyncker.github.io/fractals/render/pic17.png
ζ(|Re(z)| + |Im(z)|*i) + 0 https://asyncker.github.io/fractals/render/pic21.png
ζ(|Re(z)| + |Im(z)|*i) + 1/(-0.724775731 + 0i) https://asyncker.github.io/fractals/render/zeta-inv-conj-burning-ship-0.724775731.png
ζ(z) + c https://asyncker.github.io/fractals/render/zeta-mandelbrot-zoom.png
zcosh(z, 1/2) + c https://asyncker.github.io/fractals/render/zcosh-mandelbrot-zoom.png
zsinh(z, 1/2) + c https://asyncker.github.io/fractals/render/zsinh-mandelbrot-zoom.png
ln(sin(1 / (|Re(z)| + |Im(z)|*i))) + c (c ~= -0.46706709702891 + 0.0083333333333333i) https://asyncker.github.io/fractals/render/log_sin_test.png
zeta(z ^ 0.27) + 0 https://asyncker.github.io/fractals/render/zeta_pow.png
exp(z ^ 0.27) + 0 https://asyncker.github.io/fractals/render/exp_pow.png

zeta сложно сделать через quaternion, но легко через bicomplex в 4d, удобно что в bicomplex уже зашито 2 комплексных параметра и есть идемпотентность. Отобразить zeta в гильбертовом пространстве/эрмитовы операторы является сложной задачей. Ещё нужны мультипликативные интегралы и производны не-ньютоновские исчисления. И многозначные функции arcgamma

Идея создать алгебру, которая включает/объединяет элементы: p-adic, неархмедовых, гиперреальных, многочлены Лорана, кольцо Лорана. Всё начинается с +-*/^root (положительные, отрицательные, дробные, -, иррациональные, комплексные) и прочерк закроют новые числа:
ω^-1 = ε
ε^-1 = ω
+∞ > ω > 10^1000000
+0 < ε < 10^-1000000
ω, ε отображают масштаб (ω^-7 * 6.246) вот https://asyncker.github.io/fractals/render/scale_plane_algebra.png
0.999999... * ω = ...999999.0 и 1 * ω = ω теперь интервал не [0, ε], а [0, 1] выходит между 0.999999... и 1 несчётно много чисел
(ω - 1) * 1/ω = 1 - ε (ω являются решением уравнения (x - 1) * 1/x = 0.999999...)

Можно задать примерные значения ε ~= 0.001 и ω ~= 1000, это прикладной смысл:
ln(ε) = -ln(ω)
ln(ω) = -ln(ε)
ln(ω^ε) = -ε * ln(ε)
ε * ω = 1
15 * ω^3 * ε^2 + 3 * ω = 18ω
nround(+ε) = +0
around(-∞) = -ω
