from math import *

# faça seu código aqui!
lado = float(input())
apotema = lado/(2.0* tan(pi/8.0))
area = float(4*lado*apotema)
print(round(area,2))