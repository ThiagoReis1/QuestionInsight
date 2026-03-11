from math import *

raio_da_fazenda = float(input())

custo_por_m2= float(input())

area_da_fazenda= pi * raio_da_fazenda**2

custo_total= area_da_fazenda * custo_por_m2



print(round(custo_total,2))