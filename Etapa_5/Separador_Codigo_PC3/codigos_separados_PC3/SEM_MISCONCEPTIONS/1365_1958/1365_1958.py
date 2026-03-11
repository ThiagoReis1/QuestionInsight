from math import*

angulo = radians(float(input('Angulo da flecha:')))
distancia = float(input('Distancia em metros:'))
g = 9.8
vi = ((sqrt(distancia*g / sin(2*angulo))))
print(round(vi, 2))