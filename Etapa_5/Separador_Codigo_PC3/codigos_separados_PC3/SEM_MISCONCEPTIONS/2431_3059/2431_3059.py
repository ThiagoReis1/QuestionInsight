"""
Introducao a Programacao de Computadores
Trabalho Pratico 01 - Variaveis e Estrutura Sequencial
Versao C
Desconto na Passagem
Criado em 27 / 02 / 2018
@author: IComp / UFAM
"""

#constantes
taxaDesconto = 35

#entradas
precoCliente = float(input("Valor da passagem do cliente: "))
precoAcompanhante = float(input("Valor da passagem do acompanhante: "))

#processamento
precoDesconto = precoAcompanhante - (precoAcompanhante * (taxaDesconto / 100))

#saidas
print(round(precoCliente, 2))
print(round(precoDesconto, 2))
print(round(precoCliente + precoDesconto,2))