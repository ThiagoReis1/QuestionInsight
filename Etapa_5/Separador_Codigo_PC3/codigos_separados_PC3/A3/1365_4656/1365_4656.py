from math import*
angulo = float(input("angulos da flecha"))
distancia = float(input("distancia"))
g = 9.8
v = sqrt(distancia*(g/sin(2*angulo)))
