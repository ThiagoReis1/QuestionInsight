from math import *

lado = float(input("insira o comprimento do lado do heptagono: "))

apotema = lado / (2 * tan(pi / 7))
area = (7 * lado * apotema) / 2

print(round(area, 2))