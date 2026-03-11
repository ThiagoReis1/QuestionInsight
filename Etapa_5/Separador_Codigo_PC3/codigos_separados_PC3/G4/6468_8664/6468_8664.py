from math import *

# faça seu código aqui!

lado = int(input("O valor do lado do pentagono: "))


den = 2*tan(pi/5)
apt = lado/den
ap = (5*lado*apt)/2


print(round(ap, 2))
