#-------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# MAURÍCIO NAOTO HANDA MITOSO
# DATA: 16/06/2016
#
# OBJETIVO: Escrever um programa que leia o comprimento dos lados
# do terreno (em metros), e o custo de construção da cerca por metro, retornando
# como saída o custo total do serviço para envolver toda a roça.
#-------------------------------------------

#medida dos lados
lado_a = float(input("Qual o tamanho do lado A(em metros)? "))
lado_b = float(input("Qual o tamanho do lado B(em metros)? "))
lado_c = float(input("Qual o tamanho do lado C(em metros)? "))
#custo da construcao
custo_m = float(input("Qual o custo da construcao da cerca por m? "))
#custo total
custo_total = (lado_a + lado_b + lado_c) * custo_m

print (round(custo_total, 2))


