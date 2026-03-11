from math import *

c = int(input("Digite o comprimento do lado do decagono:"))

apotema = c/(2*tan(pi/10))
area = 5*c*apotema

print (round(area,2))