from math import *

raioAproximado = float(input())
custo = float(input())

area = pi * (raioAproximado ** 2)
custoTotal = area * custo

print(round(custoTotal, 2))