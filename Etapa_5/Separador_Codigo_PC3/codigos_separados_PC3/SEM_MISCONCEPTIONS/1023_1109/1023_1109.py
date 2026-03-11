from math import *
raio = float(input("Digite o raio: "))
custo_metro = float(input("Digite o custo por m: "))
perimetro = 2 * pi * raio
custo_total = perimetro * custo_metro
print(round(custo_total, 2))