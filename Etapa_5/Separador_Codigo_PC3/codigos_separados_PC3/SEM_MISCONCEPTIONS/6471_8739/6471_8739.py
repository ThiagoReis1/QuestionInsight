from math import*

lado = float(input("comprimento dos lados: "))

apotema = lado / (2 * tan (pi /  8))

area = 4 * lado * apotema

print(round(area, 2))