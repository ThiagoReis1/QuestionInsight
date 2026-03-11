from math import *
lado = float(input("Digite um numero: "))

apotema = lado/ 2 * tan(pi/12)
AD = 6 * lado * apotema

print(round(AD, 2))