from math import tan, pi
lado = int(input("digite o comprimento do lado: "))
apotema = lado / (2 * tan (pi / 7))
area = 7 * lado * apotema / 2

print(round(area, 2))