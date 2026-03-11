from math import *

ang = float(input("Digite o angulo da flecha: "))
d = float(input("Digite a distancia entre voce e a criatura: "))
g = 9.8

V = sqrt(d*(g/(sin(radians(2*ang)))))
print(round(V,2))
