# Talita Oliveira Gomes Passos
# Matricula: 21552161
# 16 de Junho de 2016
# Exercicio 1 da avaliacao

from math import *

# Raio do circulo e da fazenda
raio = float(input("Digite o raio: "))

# Area do circulo e da fazenda
area_da_fazenda = pi * raio ** 2

# Custo da aplicacao de fertilizante por m2
custo_m2 = float(input("Digite o custo: "))

# Custo total da aplicacao de fertilizante
custo_total = area_da_fazenda * custo_m2

print(round(custo_total, 2))