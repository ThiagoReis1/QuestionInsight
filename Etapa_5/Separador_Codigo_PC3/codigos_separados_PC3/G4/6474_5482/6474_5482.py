from math import *

# faça seu código aqui!
lado = float(input("escreva o valor do lado: "))
ang = tan(pi/11)
apo = lado/(2*ang)
area = (11*lado*apo)/2
print(round(area, 2))