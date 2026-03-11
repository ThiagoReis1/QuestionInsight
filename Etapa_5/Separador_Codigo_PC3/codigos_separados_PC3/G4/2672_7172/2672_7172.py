from math import*
r=float(input("raio r do poligono regular: "))
n=int(input("numero de lados n: "))
A=1/2*((r*cos(pi/n))**2*tan(pi/n))
print(round(A,2))