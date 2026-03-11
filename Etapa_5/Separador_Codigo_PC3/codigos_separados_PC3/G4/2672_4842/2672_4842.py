from math import *
r = float(input("DIgite o valor do raio: "))
n = int(input("Digite o numero de lados: "))
A = 1/2*((r*cos(pi/n))**2*tan(pi/n))
print(round(A, 2))