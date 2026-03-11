vel = float(input('velocidade inicial(v0)'))
dist = float(input('distancia(d)'))
import math
x = dist*(9.8/vel**2)
y = 90/math.pi
ang = math.asin(x)*y
print(round(ang , 2))