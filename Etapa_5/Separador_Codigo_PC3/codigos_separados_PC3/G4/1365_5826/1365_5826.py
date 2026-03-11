from math import *

ang = float(input("Digite o angulo da flecha: "))
dist = float(input("Digite a distancia entre voce e o monstro: "))

g = 9.8
v0 = sqrt((dist*(g/sin(2*radians(ang)))))

print(round(v0,2))