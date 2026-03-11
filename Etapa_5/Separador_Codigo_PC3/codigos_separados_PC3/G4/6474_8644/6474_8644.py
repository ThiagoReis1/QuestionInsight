from math import *

# faça seu código aqui!
l = int(input("comprimento do lado: "))

x = l / (2*(tan(pi/11)))

A = (11 * l * x)/2

print(round(A, 2))