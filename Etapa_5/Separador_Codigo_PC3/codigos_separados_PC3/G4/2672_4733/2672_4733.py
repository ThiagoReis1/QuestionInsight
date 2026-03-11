from math import*

r=float(input("digite o raio"))
l=int(input("numero de lados"))

A=1/2*((r*cos(pi/l)))**2*tan(pi/l)

print(round(A, 2))