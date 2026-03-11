from math import *
import math

# faça seu código aqui!

L = float (input ("digite quanto vale o lado do decagono:"))

apo = L / ( 2 * tan (math.pi / 10) )

Area = 5 * L * apo

print ( round (Area, 2))