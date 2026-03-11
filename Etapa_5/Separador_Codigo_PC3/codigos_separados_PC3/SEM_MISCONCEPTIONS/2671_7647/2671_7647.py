from math import pi
from math import cos

raio = float(input("Insira o Valor do Raio: "))
n_lados = int(input("Insira o Numero de Lados do Poligono: "))

a = raio * cos(pi/n_lados)

print(round(a, 2))