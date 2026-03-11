from math import *

aluguel = 50.00
taxa = 30.00

dias_alugados = float(input("Digite a quantidade de dias alugados: "))

valor_total = (dias_alugados * aluguel + taxa) * 1.18

print(round(valor_total, 2))