from math import *
angulo=float(input("angulo da flecha:"))
alpha=radians(angulo)
distancia=float(input("distancia:"))
seno=sin(2*alpha)
g=9.8
velocidade=(sqrt((distancia*g)/seno))
print(round(velocidade,2))