from math import*
raio = float(input("valor do raio: "))
N = float(input("numero de lados: "))
apotema = raio*cos(pi/N)
print(round(apotema,2))