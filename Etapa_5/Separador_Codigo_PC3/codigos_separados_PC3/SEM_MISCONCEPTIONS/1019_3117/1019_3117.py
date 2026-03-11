from math import *
#entradas
largura_fazenda = float(input("largura: "))
comprimento_fazenda = float(input("comprimento: "))
custo_por_m2 =  float(input("custo por m2: "))

#area da fazenda
area_da_fazenda = largura_fazenda * comprimento_fazenda

#custo por m2
custo_total = area_da_fazenda * custo_por_m2

#saida

print(round(custo_total,2))