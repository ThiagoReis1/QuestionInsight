from math import *
raio = float(input("Digite o raio: "))
lados = int(input("Digite o numero de lados: "))
L = 2*raio*sin(pi/lados)
print(round(L,2))