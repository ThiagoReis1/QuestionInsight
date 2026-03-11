from math import *

# faça seu código aqui!

l = float(input("lados do pentagono: "))

apotema = l/(2*tan(pi/7))
a_h = (7 * l * apotema)/2

print(round(a_h,2))