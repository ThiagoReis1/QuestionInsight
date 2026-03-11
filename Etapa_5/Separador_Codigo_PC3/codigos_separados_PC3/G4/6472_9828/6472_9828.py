from math import *

l = float(input("Informe o comprimento do lado do Eneagono: "))
a = l/(2*tan(pi/9))
AE = (9*l*a)/2

print(round(AE,2))