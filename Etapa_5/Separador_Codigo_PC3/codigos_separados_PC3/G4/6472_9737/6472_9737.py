from math import *

lado = int(input("Comprimento do lado: "))
aptm = lado/(2*(tan(pi/9)))
area = (9*lado*aptm)/2
print(round(area,2))