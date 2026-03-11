from math import *

raio = float(input(" raio R: "))

lados = float(input(" lados do poligono: "))

cosseno = cos( pi / lados)

a = raio * cosseno

print(round( a , 2))