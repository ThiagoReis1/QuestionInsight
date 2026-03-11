from math import*
r = float(input("raio: "))
n = float(input("lados: "))
a = pi/n
b = cos(a)
c = tan(a)
A = (1/2)*((r*b)**2)*c
print(round(A, 2))