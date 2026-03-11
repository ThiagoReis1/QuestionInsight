#determinar as entradas
r = float(input("Qual o valor do raio r? "))
n = int(input("Quantos lados a figura possui? "))

#determinar a area
from math import *
c = cos( pi / n )
a = ( r * c ) ** 2
t = tan( pi / n)
a = (1/2) * (a * t)
print(round(a,2))