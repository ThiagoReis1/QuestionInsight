from math import *

# faça seu código aqui!
lado = float(input("lado do dodecagono: "))
apotema = lado/(2*tan(pi/12))
areaD = 6*lado*apotema
print(round(areaD, 2))