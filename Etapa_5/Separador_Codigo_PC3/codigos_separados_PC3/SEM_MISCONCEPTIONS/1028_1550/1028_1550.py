from math import *
consumo= float(input("digite o consumo do mês:"))
round(consumo,2)
custo = (consumo * 0.37) + 15.00
custo_t= (custo*0.35)
custo_total= (custo+custo_t)
print(round(custo_total,2))