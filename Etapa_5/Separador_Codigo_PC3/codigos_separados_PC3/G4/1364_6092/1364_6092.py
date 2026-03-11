from math import *
#valor da gravidade #

g = 9.8
# entrada 

v= float(input(""))
d= float(input(""))

a = asin(d*g/v**2)*90/pi 

print(round(a,2))
