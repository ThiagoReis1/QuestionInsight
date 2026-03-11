from math import *
raio_circulo = float(input("raio do circulo   "))
custo_de_aplicacao_m2 = float (input("custo de aplicacao por metro quadrado    "))
custo_total = pi * (raio_circulo ** 2) * custo_de_aplicacao_m2
print(round(custo_total,2))