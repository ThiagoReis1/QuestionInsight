# Universidade Federal do Amazonas
# Polyana Almeida da SIlva - 21551333
# Lab ICC - Avaliacao 1
# Data: 16/06/16

cateto1 = float(input("Qual o comprimento do cateto?"))
cateto2 = float(input("Qual o comprimento do cateto?"))
custo_aplicacao = float(input("Qual o custo de aplicacao do fungicida?"))

area_triangulo = cateto1 * cateto2 / 2
custo_total = round (area_triangulo * custo_aplicacao, 2)

print(custo_total)