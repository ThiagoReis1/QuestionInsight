from math import *
litros = float(input(" Qual a valor a ser pago"))
preco_litro = 2.86
preco_oleo = 50
litrosq = 10
porcentagem = 34/100
preco_total = preco_litro + preco_oleo
icms = preco_total * porcentagem
valor = preco_total + icms
print(round(valor,2)

