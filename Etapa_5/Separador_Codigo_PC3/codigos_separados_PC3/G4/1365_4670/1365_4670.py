from math import*
ang = radians(float(input("angulo: ")))
dist = float(input("distancia: "))
g = 9.8
velo = sqrt(dist*(g/sin(2*ang)))
print(round(velo, 2))