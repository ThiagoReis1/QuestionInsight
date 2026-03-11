from math import *

# faça seu código aqui!

lado = float(input('imprima o lado do decagono: '))
apotema = lado/(2*tan(pi/12))
area = 6 * lado * apotema

print(round(area , 2))