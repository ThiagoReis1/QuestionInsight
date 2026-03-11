from math import*
r = float(input("Raio: "))
n = int(input("Numero de lados: "))
x = r * cos(pi/n)
print(round(x, 2))