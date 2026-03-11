#ler: comp da aresta 
#ler: custo da aplicacao 
#saida: custo total
#area: 2 * (a ** 2) * sqrt(2 + 1)
comp_aresta = float(input("Digite: "))
custo_aplicacao = float(input("Digite: "))
from math import *
area = (2) * (comp_aresta ** 2) * (sqrt(2) + 1)
custo_total = area * custo_aplicacao
print(round(custo_total, 2))