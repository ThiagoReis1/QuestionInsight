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
peso = float(input("Entre com o peso do produto: "))
distancia = float(input("Entre com a distancia: "))

#processamento
preco = (peso * kilo) + (distancia * km)
preco_icms = preco * (icms / 100)
preco_total = preco + preco_icms

#saidas
print(round(preco_total,2))