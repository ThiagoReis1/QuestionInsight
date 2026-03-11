from math import *

# faça seu código aqui!

L = float(input("Comprimento do lado: "))

A = L / (2 * tan(pi/10))
AD = 5 * L * A

print(round(AD, 2))