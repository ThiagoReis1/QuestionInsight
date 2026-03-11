from math import*
raio = float(input("raio da fazenda:"))
custo = float(input("custo:"))

area = pi*raio**2
custoT = area * custo

print(round(custoT,2))