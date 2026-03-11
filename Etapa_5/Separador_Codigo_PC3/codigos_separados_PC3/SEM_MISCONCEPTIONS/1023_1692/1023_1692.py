#Wagner William Amorim - Matricula 21552149
#Primeira Avaliação
#Exercicio 1
#16/06/2016

raio = float (input("Digite o valor do raio: "))

from math import pi

perim = (2 * pi* raio)

custo_da_construcao = float (input("Qual o custo para essa construcao ? "))

custo_total = perim * custo_da_construcao

print (round(custo_total,2))