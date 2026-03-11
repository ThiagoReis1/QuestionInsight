A = float(input("Qual o angulo da flecha ao sair do arco? "))
B = float(input("Qual a distancia da criatura Falmer em metros? "))

from math import *
Vo = radians(D*9.8/sen(2*A))


print(Vo(round,2))
