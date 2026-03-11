"""
Introducao a Programacao de Computadores
Trabalho Pratico 01 - Variaveis e Estrutura Sequencial
Versao B
Financeira
Criado em 27 / 02 / 2018
@author: IComp / UFAM
"""

#constantes
taxaJuros = 3

#entradas
capital = float(input("Entre com o valor da compra:"))
tempo = int(input("Entre com a qt de parcelas:"))

#processamento
juros = float((capital * taxaJuros * tempo) / 100)
montante = capital + juros

#saidas
print(round(montante,2))
