from math import *

a = float(input("digite o valor a: "))

custo_aplicacao = float(input("custo da aplicacao: "))

area_octogono = (2 * (a**2) * (sqrt(2) + 1))


custo_total = area_octogono * custo_aplicacao
 
print(round(custo_total, 2))