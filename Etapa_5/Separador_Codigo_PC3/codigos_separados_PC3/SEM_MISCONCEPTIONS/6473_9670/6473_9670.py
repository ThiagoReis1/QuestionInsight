from math import *

lado= float(input("digite o comprimento do decagono"))

apotema= lado/(2*tan(pi/10))

areadecagono= 5*lado*apotema

print(round(areadecagono, 2))