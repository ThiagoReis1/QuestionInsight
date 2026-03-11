from math import *
a = float(input("Digite o comprimento:"))
custo_metro = float(input("Digite o custo por metro quadrado:"))
A = 3*(sqrt(3))*((a**2)/2)
custo_total= custo_metro * A
print(round(custo_total, 2))