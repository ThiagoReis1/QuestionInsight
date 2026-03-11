from math import *

# faça seu código aqui!

lado = int(input("Digite o comprimento dos lados:"))

from math import*
apotema = lado / (2*tan(pi/12))
area = 6*lado*apotema

print(round(area,2))