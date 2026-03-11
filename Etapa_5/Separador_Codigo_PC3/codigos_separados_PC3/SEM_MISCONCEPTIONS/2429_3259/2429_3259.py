"""
Introducao a Programacao de Computadores
Trabalho Pratico 01 - Variaveis e Estrutura Sequencial
Versao A
Restaurante
Criado em 27 / 02 / 2018
@author: IComp / UFAM
"""
#entradas
guarnicao = int(input("qt de gaurnicao: "))
bebida = int(input("qt de bebidas: "))

#constantes
precoOpcaoPrincipal = 6.90
precoGuarnicao = 2.50
precoBebida = 3.00


#processamento
valor = precoOpcaoPrincipal + (guarnicao * precoGuarnicao) + (bebida * precoBebida)

#saidas
print(round(valor,2))