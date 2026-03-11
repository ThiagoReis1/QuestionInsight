from math import *
r= float(input("Raio r: "))
n= int(input("Numero de lados n: "))
A= 1/2 * ((r* cos(pi/n))**2 * tan(pi/n))
print(round(A, 2))