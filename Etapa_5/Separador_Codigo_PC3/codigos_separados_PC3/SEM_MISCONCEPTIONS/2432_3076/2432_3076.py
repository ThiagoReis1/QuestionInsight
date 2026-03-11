"""
Introducao a Programacao de Computadores
Trabalho Pratico 01 - Variaveis e Estrutura Sequencial
Versao D
Imobiliaria
Criado em 27 / 02 / 2018
@author: IComp / UFAM
"""

#entradas
precoArea = float(input("preco area m2: "))
ap = int(input("metragem da area privativa m2: "))
ac = int(input("metragem da area comum m2: "))
ag = int(input("metragem da area garagem m2: "))


#processamento
precoTotal = float(((ap + ac + ag) * precoArea))

#saidas
print(round(precoTotal,2))