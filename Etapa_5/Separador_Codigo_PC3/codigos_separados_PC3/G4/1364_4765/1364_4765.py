from math import *
g = 9.8
Vo = float(input("Velocidade"))
S = float(input("S"))
arco = asin(S*(g/Vo**2))
div = 90/pi
angulo = arco*div
print(round(angulo,2))