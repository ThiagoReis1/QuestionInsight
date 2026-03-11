Vo = float(input("Digite a velocidade inicial "))
d = float(input("Digite a distancia entre em metros"))


g = 9.8


from math import asin
from math import pi

a = asin(d * g / Vo**2) * 90 / pi

print(round(a, 2))

