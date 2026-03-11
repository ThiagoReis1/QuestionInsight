from math import *

l= float(input("comprimento do lado do dodecagono: "))

apotema= l/(2*tan(pi/12))
a= 6*l*apotema


print(round(a, 2))
# faça seu código aqui!