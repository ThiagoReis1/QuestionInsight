from math import*
a = float(input("Digite o cumprimento"))
custo_metro = float(input("Digite o custo por metro quadrado"))
A = 6*a
custo_total = custo_metro * A
print(round(custo_total,2))
