from math import *
a = float(input("Qual e o comprimento da aresta?"))
custo= float(input("Qual e o custo do fertilizante?"))
area = (3 * sqrt(3) * (a**2 / 2))
custo_total = custo * area    
print(round(custo_total, 2))