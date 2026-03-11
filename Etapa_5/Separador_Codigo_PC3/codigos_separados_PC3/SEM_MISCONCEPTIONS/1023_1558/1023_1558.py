valor_raio = float(input("Qual o valor do raio? "))
custo_por_metro = float(input("Qual o valor do raio? "))
from math import*
perimetro_circunferencia = 2 * pi * valor_raio
custo_da_construcao = perimetro_circunferencia * custo_por_metro
print(round (custo_da_construcao, 2))