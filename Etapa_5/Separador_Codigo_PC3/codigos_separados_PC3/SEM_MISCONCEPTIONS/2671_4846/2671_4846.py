raio=float(input("Digite o raio:"))
lados=int(input("Digite a quantidade de lados:"))

from math import *

a=raio * cos(pi/lados)

print(round(a,2))