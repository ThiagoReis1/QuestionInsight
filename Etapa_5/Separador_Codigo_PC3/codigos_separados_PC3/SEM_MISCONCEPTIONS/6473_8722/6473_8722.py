from math import *
# faça seu código aqui!

lado = float(input("Qual o valor do lado? "))

apotema = float(lado/(2*tan(pi/10)))

area = 5*lado*apotema

print(round(area,2))