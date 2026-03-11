"""
Introducao a Programacao de Computadores
Trabalho Pratico 01 - Variaveis e Estrutura Sequencial
Versao A
Restaurante
Criado em 27 / 02 / 2018
@author: IComp / UFAM
"""

#constantes
precoOpcaoPrincipal = 6.90
precoGuarnicao = 2.50
precoBebida = 3.00

#entradas
qtdeGuarnicao = int(input("qt guarnicoes: "))
qtdeBebida = int(input("qt bebidas: "))

#processamento
valor = precoOpcaoPrincipal + (qtdeGuarnicao * precoGuarnicao) + (qtdeBebida * precoBebida)

#saidas
print(round(valor,2))