from math import *

O = float(input("O comprimento do lado do octogono:"))
A = O/(2*tan(pi/8))
C = (4*O*A)

print(round(C,2))