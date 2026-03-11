"""
Introducao a Programacao de Computadores
Trabalho Pratico 01 - Variaveis e Estrutura Sequencial
Versao G
Ecommerce
Criado em 27 / 02 / 2018
@author: IComp / UFAM
"""

#constantes
desconto40 = 40
desconto5 = 5

#entradas
preco = float(input("Entre com o valor do produto: "))

#processamento
frete = preco * (desconto5 / 100)
precoComDesconto = preco - (preco * (desconto40 / 100))

#saidas
print(round(precoComDesconto,2))
print(round(frete,2))