from math import*
a = float(input("digite o valor de a:"))
b = float(input("digite o valor de b:"))
custo_metro = float(input("digite o valor do custo por n= "))
area_do_triangulo = (a * b) / 2
custo_total = area_do_triangulo * custo_metro
print(round(custo_total,2))