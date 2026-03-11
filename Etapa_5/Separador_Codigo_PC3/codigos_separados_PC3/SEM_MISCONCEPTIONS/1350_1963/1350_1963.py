# Dina Karen Barros Vieira
# Trabalho Prático 1
# exercício 1

qtd_arv = float(input("Qual a estimativa de árvores por m2?"))
comp_s_maior = float(input("Qual o comprimento do semieixo maior?"))
comp_s_menor = float(input("Qual o comprimento do semieixo menor?"))

from math import*

area_elip = pi * comp_s_maior * comp_s_menor
qtd_total_arv = area_elip * qtd_arv

print (int(round(qtd_total_arv, 2)))