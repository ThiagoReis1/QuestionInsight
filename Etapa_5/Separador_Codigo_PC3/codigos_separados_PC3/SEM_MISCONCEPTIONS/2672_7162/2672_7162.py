from math import *

# Informações
raio = float(input("Digite o valor do raio:"))
n_lados = int(input("Qual o numero de lados?"))

# Cálculo da área
area = 1/2 * (raio * cos(pi/n_lados))**2 * (tan(pi/n_lados))

#Saída
print(round(area,2))