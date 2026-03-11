v=float(input("Velocidade da flecha: "))
d=float(input("Distancia: "))

from math import*
g= 9.8
ac=asin((d*g)/(v**2))
angulo= ac*90/pi

print(round(angulo,2))