"""
Introducao a Programacao de Computadores
Trabalho Pratico 01 - Variaveis e Estrutura Sequencial
Versao I
Bolsa de Valores
Criado em 27 / 02 / 2018
@author: IComp / UFAM
"""

#entradas
precoAbertura = float(input("Preco de abertura: "))
precoFechamento = float(input("Preco de fechamento: "))

#processamento
diferenca = precoFechamento - precoAbertura
percentual = (diferenca * 100) / precoAbertura

#saidas
print(round(percentual,2))