from math import *

lado = int(input("insira o comprimento do lado do poligono"))
apotema = lado / (2* tan(pi/6))
area = (3 * lado) * apotema
print(round(area, 2))