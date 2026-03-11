#Leitura dos dados
aresta = float(input("Digite o comprimento da fazenda: "))
custo = float(input("Digite o valor do custo: "))

#Cálculo do custo total
from math import *
area = 2 * aresta ** 2 * (sqrt( 2) + 1 )
custo_total = area * custo

print(round(custo_total, 2))