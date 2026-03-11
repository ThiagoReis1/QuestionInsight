from math import*

a=float(input("Digite o angulo da flecha: "))
d=float(input("Digite a distancia: "))

graus= radians(a)

g = 9.8

v = sqrt((d*g)/ sin(2*graus))

print(round(v,2))