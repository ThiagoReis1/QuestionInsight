#Lucas de Sousa Martins
#16/06/2016
from math import *
a = float(input("Insira o comprimento da aresta: "))
f = float(input("Insira o custo do fertilizante: "))
area = 2 * (a ** 2 ) * (sqrt(2) + 1 )
servico = area * f
print(round(servico,2))