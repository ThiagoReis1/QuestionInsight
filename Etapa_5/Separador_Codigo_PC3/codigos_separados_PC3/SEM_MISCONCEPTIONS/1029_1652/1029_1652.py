#-------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# RODRIGO FONTANELLA CESTARI
# DATA: 16/06/2016
#
# OBJETIVO: Escreva um programa que leia o
# consumo de chamadas (em minutos) durante certo mês e
# determine o valor a ser pago.
#-------------------------------------------

#quantidade de minuto
minuto = float(input("quantos minutos ? "))

valor_minuto = 0.28
valor_fixo = 23.0
imposto = 0.31
#valor conta por minuto mais taxa fixa
valor_conta = (minuto * valor_minuto) + valor_fixo
#valor conta com icms
valor_com_taxa = valor_conta + (valor_conta * imposto)
print(round(valor_com_taxa, 2))