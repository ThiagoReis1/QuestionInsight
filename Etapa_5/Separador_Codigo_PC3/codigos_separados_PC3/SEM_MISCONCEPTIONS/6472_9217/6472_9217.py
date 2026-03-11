from math import *

ld_eneagono = float(input("Digite o comprimento do lado do eneagono: "))

apotema = ld_eneagono / (2 * tan(pi/9))

area = 9 * ld_eneagono * apotema / 2
print(round(area, 2))
