from math import*

m = float(input('informe estimativa de macas: '))
a = float(input('informe o comprimento da aresta: '))

h = 3 * ((sqrt(3*a*a) / 2))
t = int(m * h)

print(t)

