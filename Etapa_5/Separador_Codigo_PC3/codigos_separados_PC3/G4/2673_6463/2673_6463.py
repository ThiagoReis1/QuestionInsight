from math import *

raio = float(input("Qual o valor do raio: "))
lado = int(input("Quantidade de lados: "))

L = 2 * raio
total = L * sin(pi/lado)

print(round(total,2))