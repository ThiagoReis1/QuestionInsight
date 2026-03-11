"""
Introducao a Programacao de Computadores
Trabalho Pratico 01 - Variaveis e Estrutura Sequencial
Versao H
Correios
Criado em 27 / 02 / 2018
@author: IComp / UFAM
"""

#constantes
kilo = 25.00
km = 0.10
icms = 12

#entradas
peso = int(input("Entre com o peso do produto: "))
distancia = int(input("Entre com a distancia: "))

#processamento
preco = (peso * kilo) + (distancia * km)
precoICMS = preco * (icms / 100)
precoTotal = preco + precoICMS

#saidas
print(round(precoTotal,2))