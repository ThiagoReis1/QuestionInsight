from math import *
a = float(input("comprimento do lado do hexano:"))
b = a/(2*tan(pi/6))
area = 3*a*b
print(round(area, 2))
