from math import * 
angulo = float(input())
velocidade = float(input())
Vo = velocidade
a = radians(angulo)
g = 9.8
d = (Vo**2 * sin(2 * a)) / g
print(round( d , 2))