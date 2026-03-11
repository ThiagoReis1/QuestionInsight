from math import *

lado=float(input("comprimento hexagono: "))

apotema= lado/(2*tan(pi/6))
areahex= (3 * lado * apotema)

print(round(areahex, 2))