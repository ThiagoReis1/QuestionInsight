a = float(input("aresta: "))
p = float(input("valor fertilizante: "))
from math import*
area = 3*(3**0.5)*(a**2)/2
custo = area*p
print(round(custo,2))