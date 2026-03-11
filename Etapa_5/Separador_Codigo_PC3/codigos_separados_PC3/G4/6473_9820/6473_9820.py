from math import *
#ent =comprimento do lado 
#sai = area 

lado = float(input("comprimento do lado:"))

apo = (lado /(2 * tan(pi/10)))

area = round(5 * lado * apo,2)

print (area)
