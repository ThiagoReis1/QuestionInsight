from math import*
r= float(input("Digite o valor do raio: "))
n= float(input("Digite o numero de lados: "))

L=2*r*sin(pi/n)
print(round(L,2))