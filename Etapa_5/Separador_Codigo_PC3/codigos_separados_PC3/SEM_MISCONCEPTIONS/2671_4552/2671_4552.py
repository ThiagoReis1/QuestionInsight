from math import *

raio = float(input())
lados = int(input())

apotema = raio * (cos(pi/lados))

print(round(apotema,2))