from math import *

lado = float(input("Entre com o valor do comprimento do lado do eneagono: "))

ap = lado / (2 * tan(pi/9))
areae = (9 * lado * ap) / 2 

print(round(areae, 2))