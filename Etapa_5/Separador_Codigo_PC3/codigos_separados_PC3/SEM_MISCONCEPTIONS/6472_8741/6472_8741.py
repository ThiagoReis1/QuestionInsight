from math import *
lado = int(input("comprimento do lado do eneagono? "))
lado2 = tan(pi/9)
apotema = lado / (lado2  * 2)
area = (9 * lado * apotema) / 2
print(round(area, 2))