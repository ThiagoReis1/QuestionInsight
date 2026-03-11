from math import *

# faça seu código aqui!

ld = float(input("comprimento lado: "))

apt = ld / (2 * tan(pi / 9))

area = (9 * ld * apt) / 2

print(round(area, 2))