from math import*

r = float(input("raio: "))
n = int(input("numero de lados: "))

x = (r * cos(pi/n))**2
y = tan(pi/n)


A = (1/2)*x*y

print(round(A, 2))