from math import *

EG = float(input('escreva a quantidade estimada de gramas - '))
Gc = float((EG / 5) * sqrt(9/5)) 
Ga = float(((EG ** 2) / pi))
Got = float(sqrt((5 * EG) /3))
print(round(Gc, 2))
print(round(Ga,2))
print(round(Got,2))