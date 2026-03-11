from math import *

A = 6.90
B = 2.50
C = 3.00

gnc = float(input("quant de gnc: "))
bebidas = float(input("quant de bebidas: "))

tot = (gnc*B + bebidas*C + A)
print(tot)