from math import *
raio = float(input("Digite o raio: "))
custo_aplicacao = float(input("Digite o custo por metro quadrado:"))
A = pi * raio ** 2
custo_total = custo_aplicacao * A
print(round(custo_total, 2))