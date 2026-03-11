from math import*

raio=float(input("De o raio do poligono regular: "))
n=int(input("De o numero de lados do poligono regular: "))

A=1/2
B=((raio*cos(pi/n))**2)*tan(pi/n)
A=A*B
A= round(A, 2)
print(A)