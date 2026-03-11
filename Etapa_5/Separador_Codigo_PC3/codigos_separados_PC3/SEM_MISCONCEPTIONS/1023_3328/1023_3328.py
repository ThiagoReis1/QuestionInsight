from math import *
raio= float(input("valor do raio: "))
custo_por_mt= float(input("valor por mt: "))
perimetro=  (2*pi)*raio

custo_total= perimetro * custo_por_mt
print(round(custo_total, 2))