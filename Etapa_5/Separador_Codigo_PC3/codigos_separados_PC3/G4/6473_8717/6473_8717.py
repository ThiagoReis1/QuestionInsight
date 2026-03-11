from math import *
 
# faça seu código aqui!

cl = float(input("Digite o valor do lado do Decagono: "))
ap = cl / (2 * tan(pi/10))
AD = 5 * cl * ap

print(round(AD, 2))