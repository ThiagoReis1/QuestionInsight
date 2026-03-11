from math import radians, sqrt, sin

angulo = radians(float(input()))

distancia = float(input())

velocidade = sqrt(distancia * (9.8 / (sin(2*angulo))))

print(round(velocidade, 2))
