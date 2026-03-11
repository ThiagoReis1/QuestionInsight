from math import *
r= float(input("valor do raio:"))
n= int(input("numero de lados:"))
l= (2* r * sin(pi/n))
print(round(l,2))