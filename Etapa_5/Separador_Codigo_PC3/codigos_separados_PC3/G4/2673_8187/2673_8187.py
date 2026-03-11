r= float(input("raio: "))
n= int(input("numero de lados: "))
from math import*
l= 2*r*sin(pi/n)
print(round(l, 2))