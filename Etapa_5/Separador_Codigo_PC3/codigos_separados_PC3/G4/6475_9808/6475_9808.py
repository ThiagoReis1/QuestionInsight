from math import *

# faça seu código aqui!
x = float(input("O comprimento do lado do dodecagono: "))
ap = x / (2*tan(pi/12))
ad = 6*x*ap
print(round(ad,2))