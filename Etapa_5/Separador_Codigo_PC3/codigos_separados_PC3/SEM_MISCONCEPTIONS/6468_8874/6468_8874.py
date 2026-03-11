from math import *
from math import pi
from math import tan

lado = float(input("Qual e o comprimento do lado do pentagono: "))

apotema = lado/(2*tan(pi/5))

areapentagono = (5*lado*apotema)/2

print(round(areapentagono,2))

