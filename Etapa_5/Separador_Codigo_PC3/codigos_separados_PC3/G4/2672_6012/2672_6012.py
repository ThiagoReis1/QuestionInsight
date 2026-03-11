from math import*
r = float(input("raio: "))
n = int(input("lados: " ))
# formula area
a = 1 / 2 * ((r * cos(pi / n))**2 * tan(pi/n))



print(round(a,2))