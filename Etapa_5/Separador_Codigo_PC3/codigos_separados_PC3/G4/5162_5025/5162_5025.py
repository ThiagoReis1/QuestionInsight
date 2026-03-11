est = float(input("Estimativa de acaizeiros: "))
a = float(input("Comprimento da aresta: "))
from math import*
area = 3 * (sqrt(3 * (a ** 2)) / 2)
total = est * area
print(int(total))