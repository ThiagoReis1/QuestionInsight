#Kamila Dias Preira
# 16 de junho de 2016
# 1 Avaliação de ICC

from math import*

area = float(input("raio_m: "))
area_circulo = pi * area ** 2

custo_m2 = float(input(" Custo do Fertilizante: "))
custo_total = area_circulo * custo_m2

print(round(custo_total, 2))