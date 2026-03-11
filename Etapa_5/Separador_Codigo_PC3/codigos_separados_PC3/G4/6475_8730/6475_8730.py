from math import *

# faça seu código aqui!
a = float(input("Qual o comprimento do lado do dodecagono?:"))
b = 2*tan(pi/12)
op = a/b
x = 6 * a * op
print(round(x,2))
