from math import*
raio_circunferencia=float(input("raio da circunferencia"))
custo=float(input("custo por metro"))
perimetro=2*pi*raio_circunferencia
custo_total=perimetro*custo
print(round(custo_total,2))