from math import *

lado = int(input("insira o comprimento do lado do poligono: "))

apotema = lado / (2 * tan(pi/10))
area = (5 * lado) * apotema
print(round(area, 2))