from math import *

L = float(input("Digite o comprimento do lado: "))

Apt = L / (2 * tan(pi/8))
Area = 4* L * Apt

print(round(Area,2))