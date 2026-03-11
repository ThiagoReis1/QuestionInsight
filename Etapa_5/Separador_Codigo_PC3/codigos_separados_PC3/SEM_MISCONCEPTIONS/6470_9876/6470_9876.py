from math import *

# faça seu código aqui!
var1 = float(input("digite o comprimento do lado: "))
apotema = var1  / (2 * tan(pi/7))
heptagono = 7 * var1 * apotema / 2

print(round(heptagono, 2))


