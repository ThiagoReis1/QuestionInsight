"""
Introducao a Programacao de Computadores
Trabalho Pratico 01 - Variaveis e Estrutura Sequencial
Versao E
Cinema
Criado em 27 / 02 / 2018
@author: IComp / UFAM
"""

#constantes
desconto = 60

#entradas
precoIngresso = float(input("Entre com o valor do ingresso: "))

#processamento
precoAcompanhante = precoIngresso - (precoIngresso * (desconto / 100))
#valortotal
valor_total = precoIngresso + precoAcompanhante

#saidas
print(round(precoIngresso, 2))
print(round(precoAcompanhante, 2))
print(round(valor_total, 2))

