from math import*

r = float(input("raio: "))
l = int(input("lados: "))

A = 1/2*((r*cos(pi/l)))**2 * tan(pi/l)


print(round(A,2))