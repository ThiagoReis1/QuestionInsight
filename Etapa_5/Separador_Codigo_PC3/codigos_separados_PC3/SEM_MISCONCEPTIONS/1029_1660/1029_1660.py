#-------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# MAURÍCIO NAOTO HANDA MITOSO
# DATA: 16/06/2016
#
# OBJETIVO: Escrever um programa que leia o consumo de
# chamadas (em minutos) durante certo mês e
# determine o valor a ser pago.
#-------------------------------------------

#quantidade de minutos usados
qtde_minutos = float(input("Qual a quantidade de minutos que o cliente falou este mes? "))
#custo ICMS (atrelado valor final)
icms = 1.31
#valor fixo
valor_fixo = 23.00
#valor variavel
valor_variavel = 0.28 * qtde_minutos
#custo total
custo_total = (valor_fixo + valor_variavel) * icms

print(round(custo_total, 2))
