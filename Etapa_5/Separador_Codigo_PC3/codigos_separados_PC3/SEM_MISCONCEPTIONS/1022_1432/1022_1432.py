# Universidade Federal do Amazonas
# Aluno: Eules Leonardo S Lima
# Ex 01 - Calcular valor de serviço de aplicação de fertilizante
# com base na área de um octógono
from math import *
aresta = float(input("Qual o tamanho da aresta: "))
custo_por_m2 = float(input("Qual o custo da aplicação por m2: "))
area_octogono = 2 * (aresta ** 2) * (sqrt(2)+1)
custo_total = area_octogono * custo_por_m2
print(round(custo_total,2))