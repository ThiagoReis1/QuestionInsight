from math import *
raio= float(input("digite a circuferencia em metros: "))
custo= float(input("digite o total da cerca por metros: ")) 
area= (2* pi *raio)
custo_total= (area * custo)
print(round(custo_total,2))