# 16 de Junho de 2016
# kleidysson

from math import*

terreno = float (input("imprima o valor do terreno:"))
custo_m2 = float(input("imprima o valor do custo_m2:"))

raio = 2 * pi * custo_m2
custo_total = terreno * raio

print(round(custo_total, 2))
