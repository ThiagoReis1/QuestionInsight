import math

raio = float(input())
custo_aplicacao = float(input())

area = math.pi*(raio**2)

custo_total = area*custo_aplicacao
print(round(custo_total,2))
