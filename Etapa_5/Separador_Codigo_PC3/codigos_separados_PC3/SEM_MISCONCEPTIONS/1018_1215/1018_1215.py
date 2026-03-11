from math import*

a = float(input("digite o valor de a:"))
b = float(input("digite o valor de b:"))

area_triangulo = (a * b) / 2

custo_aplicacao = float(input("digite o valor do custo por metro quadrado:"))

custo_total = area_triangulo * custo_aplicacao

print(round(custo_total,2))