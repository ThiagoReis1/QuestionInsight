from math import *

lado = float(input('Digite o lado do eneagono: '))

apotema = lado / (2 * tan(pi / 9))
						
area = (9 * lado * apotema) / 2 
						
print(round(area, 2))
