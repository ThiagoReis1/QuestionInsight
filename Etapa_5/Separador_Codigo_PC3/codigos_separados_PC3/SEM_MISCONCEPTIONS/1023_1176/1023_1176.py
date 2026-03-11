#Universidade Federal do Amazonas
#ALUNO: Adriano Zeferino Ramos 
#Matricula: 21600609
# Avaliacao parcial 1
from math import *
raio= float(input("Digite o raio da circunferencia em metros: "))
custo= float(input("digite o  custo total da da cerca por metro: "))
area= (2* pi *raio)
custo_total= (area * custo)
print (round(custo_total,2))