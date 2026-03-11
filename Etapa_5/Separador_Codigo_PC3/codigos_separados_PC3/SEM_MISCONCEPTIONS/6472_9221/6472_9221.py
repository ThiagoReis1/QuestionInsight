lado= float(input("digite o comprimento do lado:"))

from math import*
apotema= lado/(2*tan(pi/9))
area= (9*lado*apotema)/2

print(round(area, 2))