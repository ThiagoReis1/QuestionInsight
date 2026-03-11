from math import*
a = float(input("digitar o raio: "))
area_circulo = pi*a**2
custo_metro = float(input("digitar o metro:"))
custo_total = area_circulo*custo_metro

print(round(custo_total, 2))

