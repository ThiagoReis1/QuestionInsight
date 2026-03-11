from math import *

# faça seu código aqui!
comprimento= float(input("lados do pentagono: "))
apotema= comprimento/ (2*tan(pi/6))
area= 3* comprimento* apotema

print(round(area, 2))