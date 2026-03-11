from math import *
raio = float(input("valor do raio:"))
lados = int(input("numero de lados:"))

l= 2*raio*sin(pi/lados)
print(round(l, 2))