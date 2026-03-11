from math import *

# faça seu código aqui!

l = float(input("Digite o lado do dodecagono aqui: "))

apotema = l / (2*tan(pi/12))

dodecagono = 6*l*apotema

print(round(dodecagono, 2))