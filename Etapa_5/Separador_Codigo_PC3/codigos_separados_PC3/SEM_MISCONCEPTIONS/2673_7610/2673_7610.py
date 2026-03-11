from math import *

r = float(input("Digite o valor do raio: "))
l = int(input("Digite o valor dos lados: "))

total = 2 * r * sin(pi/l)
print(round(total,2)) 
