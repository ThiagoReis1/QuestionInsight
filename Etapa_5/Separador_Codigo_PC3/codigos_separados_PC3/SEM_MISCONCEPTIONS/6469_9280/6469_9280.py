from math import *
lado = float(input("digite o comprimento do lado: "))
apotema = lado / (2 * (tan(3.14 / 6)))
area = 3 * lado * apotema
print(round(area, 2))