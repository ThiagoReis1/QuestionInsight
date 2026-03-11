from math import *
raio = float(input("raio r: "))
n = int(input("numero de lados: "))
A=(1/2)*((raio*cos(pi/n))**2)*tan(pi/n)
print(round(A,2))