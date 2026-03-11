from math import*
angulo= radians(float(input("angulo")))
distancia= float(input("distancia"))
g= 9.8
velocidade= sqrt (distancia * (g / sin (2 * angulo)))
print(round(velocidade, 2))