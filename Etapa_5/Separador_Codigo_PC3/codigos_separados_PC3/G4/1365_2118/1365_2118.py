from math import *

ang = float(input("valor do angulo: "))
d = float(input("valor da distancia: "))
 
ang1 = radians(ang)

g = 9.8

vo = ((d * g) / sin(2*ang1)) ** 0.5

print(round(vo, 2))



