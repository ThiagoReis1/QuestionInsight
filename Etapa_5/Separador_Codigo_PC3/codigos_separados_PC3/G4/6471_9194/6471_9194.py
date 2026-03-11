from math import *
co= float(input('comprimento do lado do octogono:'))

t= tan(pi/8)
apotema= co/ (2*t)

a= 4*co*apotema

print(round(a,2))