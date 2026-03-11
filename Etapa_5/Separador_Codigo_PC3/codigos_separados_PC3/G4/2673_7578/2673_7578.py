from math import sin
from math import pi

r=float(input("insira o valor do raio"))
n=int(input("insira o num de lados"))

l=2*r*sin(pi/n)

print(round(l,2))