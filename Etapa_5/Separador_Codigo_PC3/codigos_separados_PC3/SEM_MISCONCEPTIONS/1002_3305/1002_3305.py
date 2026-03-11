from math import *
a = float(input("entre com o valor de a: "))
custo = float(input("entre com o valor do custo: "))
area = (pi)*a**2
custo_total = (custo * area)
print(round(custo_total, 2))