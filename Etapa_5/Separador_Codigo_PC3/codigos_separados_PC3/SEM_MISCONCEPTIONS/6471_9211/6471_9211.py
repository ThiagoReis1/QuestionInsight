from math import tan, pi
lado = float(input("digite o comprimento do lado"))
apotema = lado / (2 * tan (pi / 8))
areadooctogono = 4 * lado * apotema
print(round(areadooctogono,  2))
