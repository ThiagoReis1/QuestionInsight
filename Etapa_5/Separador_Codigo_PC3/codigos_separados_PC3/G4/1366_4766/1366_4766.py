from math import *
g = 9.8
a = radians(float(input("Angulo ")))
Vo = float(input("Velocidade "))
seno = sin(2*a)
dd = float((Vo**2)*(seno))
dv = dd/g
print(round(dv,2))