from math import *

lado = float(input("digite o lado: "))

apotema = lado/(2*tan(pi/12))

AD = 6*lado*apotema

print(round(AD, 2))