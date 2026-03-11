from math import *
estimativa = float(input('Estimativa: '))
aresta = float(input('Aresta: '))
area = 3 * (sqrt(3 * (aresta ** 2)) / 2)
total = area * estimativa
print(int(total))