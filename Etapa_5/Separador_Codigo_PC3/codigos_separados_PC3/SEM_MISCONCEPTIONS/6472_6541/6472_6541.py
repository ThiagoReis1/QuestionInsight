#from math import *
import math

# faça seu código aqui!

lado = float(input())

apotema = lado/(2 * (math.tan(math.pi/9)))

areaEneagono = (9 * lado * apotema)/2

print(round(areaEneagono, 2))

