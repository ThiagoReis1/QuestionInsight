#ENTRADA

from math import*

a = float (input ("Comprimento da aresta: "))
b = float (input ("Custo de aplicacao: "))

#SAIDA

hexa = 3 * sqrt (3) * (a**2) / 2
custo_total = b * hexa


print (round(custo_total, 2))
