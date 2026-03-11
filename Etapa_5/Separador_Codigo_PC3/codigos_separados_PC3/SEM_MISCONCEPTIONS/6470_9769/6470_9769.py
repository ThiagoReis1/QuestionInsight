from math import *

# faça seu código aqui!

lado = float(input())
apotema= lado/(2 * tan(pi/7))
area= (7 * lado * apotema)/2
print(round(area,2))