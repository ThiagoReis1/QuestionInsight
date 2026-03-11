from math import *
angulo=radians(float(input("digite o angulo")))
distancia=float(input("digite o angulo"))
g=9.8
v=sqrt((distancia*g)/(sin(2*angulo)))
print(round(v,2))