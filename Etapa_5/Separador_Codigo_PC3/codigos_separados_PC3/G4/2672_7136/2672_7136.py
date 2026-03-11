from math import *
r= float(input("Digite o valor do raio: "))
n= float(input("Digite o numero de lados: "))

a= 1/2*((r*cos(pi/n))**2) * tan(pi/n)

print(round(a, 2))