from math import *

raio = float(input('digite o raio: '))
n_lados = int(input('informe quantos lados: '))

termo1 = cos((pi) / n_lados)
termo2 = tan((pi) / n_lados)
area = (1 / 2) * ((raio * termo1) ** 2) * termo2 

print(round(area, 2))