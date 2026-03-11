raio = float(input("raio:"))
lados = int(input("lados:"))

from math import*
l = 2 * raio * sin(pi/lados)

print(round(l,2))
