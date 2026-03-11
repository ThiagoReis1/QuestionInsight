from math import *

angulo = float(input())
d = float(input())

seno = sin(radians(2*angulo))

velocidade = sqrt(d * (9.8/seno))

print(round(velocidade, 2))