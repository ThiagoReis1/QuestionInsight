from math import*
raio = float(input("numero: "))
lados = int(input("n de lados: "))
L = 2 * raio * sin(pi/lados)
print(round(L, 2))