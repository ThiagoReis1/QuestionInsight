from math import *

# faça seu código aqui!

lado = float(input())
apotema = lado/(2*tan(pi/5))
areaPentagono = (5*lado*apotema)/2
print(round(areaPentagono,2))