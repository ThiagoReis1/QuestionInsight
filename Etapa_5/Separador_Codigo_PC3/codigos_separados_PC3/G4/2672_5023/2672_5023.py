from math import*
r = float(input("Valor do raio: "))
n = int(input("Numero de lados: "))
area = 1/2 * ((r * cos(pi/n))**2 * tan(pi/n))
print(round(area,2))