from math import*

r = float(input("raio: "))
n = int(input("numero de lados: "))

L = 2 * r * sin(pi/n)

print(round(L,2))


