from math import *
raio = float(input("qual o raio? "))
area = pi * raio**2
custo = float(input("qual foi o custo? "))
custo_total = area * custo

print(round(custo_total, 2))


