"""
Introducao a Programacao de Computadores
Trabalho Pratico 01 - Variaveis e Estrutura Sequencial
Versao F
Tucurui
Criado em 27 / 02 / 2018
@author: IComp / UFAM
"""

precoA = 80.0
precoB = 50.0
precoC = 30.0

#entradas
nA = int(input("No. bilhetes A: "))
nB = int(input("No. bilhetes B: "))
nC = int(input("No. bilhetes C: "))

#processamento
renda = precoA * nA + precoB * nB + precoC * nC

#saidas
print(renda)

