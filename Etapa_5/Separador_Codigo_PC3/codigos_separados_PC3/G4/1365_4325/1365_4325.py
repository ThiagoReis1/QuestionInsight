#Angulo da flecha (em graus)
from math import*

ang = float(input("Angulo da flecha ao sair do arco:"))
dist = float(input("Distancia entre objetos:"))

rad = radians(ang)
ang_2 = 2*rad

vo = sqrt(dist*(9.8/sin(ang_2)))


#Velocidade inicial
print(round(vo,2))