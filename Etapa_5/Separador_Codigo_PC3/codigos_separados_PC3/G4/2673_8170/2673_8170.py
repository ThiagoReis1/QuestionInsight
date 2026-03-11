from math import *

r = float(input("Digite o valor do raio: "))
n = int(input("Digite o numero de lados n: "))

L = 2 * r * sin(pi/n)

print(round( L , 2 ))