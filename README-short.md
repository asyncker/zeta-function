zsinh(z, t) = (ζ(t + z) - ζ(t - z)) / 2
zcosh(z, t) = (ζ(t + z) + ζ(t - z)) / 2
ζ(t + z) = zcosh(z, t) + zsinh(z, t)
ζ(t + z) * ζ(t - z) = zcosh(z, t)^2 - zsinh(z, t)^2

Нули zsinh и zcosh чередуется при t<1/2 как только t=1/2 чередование нарушается. arg(ζ(it)), её производная ~= -ln(t/2pi) и логарифм подавляет флуктуации при больших t.
zsinh_zeros[i] < zcosh_zeros[i] (все истина кроме первого при t<1/2)

Пример чередование нулей zsinh и zcosh при (t = 1/2 - 0.00001): [3.43621400, 0.81955124, 9.66691026, 14.13466233, 14.13472673, 14.51798335, 17.84559970, 20.65399921, 21.02203739, 21.02208423, 23.17028211, 25.01082878, 25.01086105, 25.49153867, 27.67018256, 29.73849079 ...]

Фракталы от zeta функции:
ζ(z) + 0 (https://raw.githubusercontent.com/asyncker/fractals/refs/heads/main/render/pic17.png)
ζ(|Re(z)| + |Im(z)| * i) + 0 (https://raw.githubusercontent.com/asyncker/fractals/refs/heads/main/render/pic21.png)
ζ(|Re(z)| + |Im(z)| * i) + 1/(-0.724775731 + 0i) (https://raw.githubusercontent.com/asyncker/fractals/refs/heads/main/render/zeta%20inv%20and%20conj%20burning%20ship%20-0.724775731.png)
ζ(z) + c (https://raw.githubusercontent.com/asyncker/fractals/refs/heads/main/render/zeta-mandelbrot-zoom.png)
zcosh(z, 1/2) + c (https://raw.githubusercontent.com/asyncker/fractals/refs/heads/main/render/zcosh-mandelbrot-zoom.png)
zsinh(z, 1/2) + c (https://raw.githubusercontent.com/asyncker/fractals/refs/heads/main/render/zsinh-mandelbrot-zoom.png)
ln(sin(1 / (|Re(z)| + |Im(z)| * i))) + c (c ~= -0.4670670970289143 + 0.008333333333333333i) (https://raw.githubusercontent.com/asyncker/fractals/refs/heads/main/render/log_sin_test.png)
zeta(z ^ 0.27) + 0: (https://raw.githubusercontent.com/asyncker/fractals/refs/heads/main/render/zeta_pow.png)
exp(z ^ 0.27) + 0: (https://raw.githubusercontent.com/asyncker/fractals/refs/heads/main/render/exp_pow.png)

Im(ζ(iz + 1/2) * ζ(-iz + 1/2)) можно создать общую функцию харди Z(x, t) и взять t = 1/2 (это и есть оригинальная функция) и t = -1/2 и получится через Im и Re сделать тоже самое.

zeta через quaternion крайнее сложно сделать, но можно взять bicomplex и отобразить zeta в 4d, зная свойства идемпотентности в bicomplex это уже 4x4 матрица так ещё к тому же коммутативная, ну и сама идея отобразить zeta в гильбертовом простнатсве/эрмитовы операторы является той самой задачей куда я копаю.

Ещё нужны мультипликативные интегралы и производны, то-есть не-ньютоновские исчисления. И идея создать многозначную функцию arcgamma.

Идея создать алгебру, которая включает/объединяет в себя элементы: p-adic, неархмедовых, гиперреальных, многочлены Лорана, кольцо Лорана. Всё начинается с +-*/^root (положительные, отрицательные, дробные числа, -, иррациональные, комплексные) видно, что есть прочерк эти новые числа и закроют этот прочерк:
w^-1 = eps
eps^-1 = w
+inf > w > 10^1000000
+0 < eps < 10^-1000000
w и eps отображают маштаба (w^-23 * 6.246) вот плоскость https://raw.githubusercontent.com/asyncker/fractals/refs/heads/main/render/scale_plane_algebra.png
0.999999... * w = ...999999.0 и 1 * w = w теперь пробел не 0 и eps, а 0 и 1 выходит между 0.999999... и 1 несчётно много чисел 
(w - 1) * 1/w = 1 - eps (w и eps являются решение уравнения (x - 1) * 1/x = 0.999999...)

Можно прикидывать примерные значения например eps ~= 0.001 и w ~= 1000:
ln(eps) = -ln(w)
ln(w) = -ln(eps)
ln(w^eps) = -eps * ln(eps)
eps * w = 1
15 * w^3 * eps^2 + 3 * w = 18w
nround(+eps) = +0
around(-inf) = -w
