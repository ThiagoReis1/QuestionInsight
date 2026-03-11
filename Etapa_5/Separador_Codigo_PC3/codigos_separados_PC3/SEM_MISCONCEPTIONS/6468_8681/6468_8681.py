lado = float(input("Insira o numero de lados: "))

from math import *

apotema = lado / (2*tan(pi/5))

areapentagono = (5*lado*apotema) / 2

print(round(areapentagono,2))
