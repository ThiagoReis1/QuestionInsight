from math import*

#Estimativa de maças por metro quadrado
estimativa = float(input("Numero de macas por metro quadrado: "))

#Comprimento da aresta
a = float(input("Aresta do campo: "))

#Area do campo
A = (3 * sqrt(3 * (a ** 2)) / 2)

#Quantidade total de maças
quantidade_total = int(estimativa * A)

print(quantidade_total)