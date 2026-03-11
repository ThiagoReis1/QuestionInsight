from math import *

raio = float(input())
custo_m = float(input())
#custo_m = round(custo_m,2)

perimetro = 2 * pi * raio
#print(perimetro)
#perimetro = round(perimetro,2)
#print(perimetro)

custo_total = custo_m * perimetro

print(round(custo_total,2))