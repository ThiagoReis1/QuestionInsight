from math import *

# faça seu código aqui!
lado = float(input("comprimento do lado do hexagono:"))
apotema = 3*lado/2*tan(pi/6)
ah = (3*lado*apotema)
print(round(ah, 2))