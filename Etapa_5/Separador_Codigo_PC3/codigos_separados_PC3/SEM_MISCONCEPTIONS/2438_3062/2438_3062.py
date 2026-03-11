"""
Introducao a Programacao de Computadores
Trabalho Pratico 01 - Variaveis e Estrutura Sequencial
Versao J
Conversor Hertz
Criado em 27 / 02 / 2018
@author: IComp / UFAM
"""

#entradas
frequencia = int(input("frequencia do sensor: "))
tempo = int(input("tempo de coleta de dados: "))

#processamento
qtdeAmostras = frequencia * (tempo * 60)

#saidas
print(qtdeAmostras)