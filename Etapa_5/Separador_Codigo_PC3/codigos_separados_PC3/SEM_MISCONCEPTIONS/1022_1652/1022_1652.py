#-------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# RODRIGO FONTANELLA CESTARI
# DATA: 16/06/2016
#
# OBJETIVO: Escreva um programa que leia o comprimento
# da aresta dessa fazenda (em metros) e o custo de aplicação 
# do fertilizante por metro quadrado, retornando como saída
# o custo total do serviço para toda a fazenda.
#-------------------------------------------

# comprimento aresta
a = float(input("aresta? "))
#custo mao de obra
custo_aplicacao = float(input("custo "))
#area do terreno
area_octogono =(2 * a**2) * ((2 ** 0.5) + 1)
# custo da obra
custo_total = custo_aplicacao * area_octogono

print(round(custo_total, 2))