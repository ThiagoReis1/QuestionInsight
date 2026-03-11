from math import*
R= float(input("valor do raio: "))
N= int(input("numeros de lados n: "))

A=1/2*((R*cos(pi/N))**2*tan(pi/N))

print(round(A, 2))