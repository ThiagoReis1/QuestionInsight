from math import*
#UNIVERSIDADE FEDERAL DO AMAZONAS
#ALUNA: LARISSA MAGNO LEAO
#MATRÍCULA:21551610
#EXERCICIO 1

a=float(input("Digite o comprimento da aresta em m:"))
custo=float(input("Digite o custo do fertilizante por m2:"))

area_hexagono=3* sqrt(3) *(a**2)/2

custo_total= area_hexagono*custo

print(round(custo_total,2))