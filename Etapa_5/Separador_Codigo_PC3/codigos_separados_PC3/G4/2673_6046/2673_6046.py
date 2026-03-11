from math import * 
 

r= float(input("digite o valor do raio: "))
n= int(input("digite o numero de lados do poligono: "))

L= 2* r* sin(pi/n)

print(round(L, 2))