from math import *
from math import sin
from math import cos
from math import acos
from math import radians
from math import tan
from math import pi

lado = int(input("Qual a medida do lado?: "))

apotema = (lado)/(2*tan(pi/5))

area_pentagono = 5*lado*apotema/2

print(round(area_pentagono, 2))
