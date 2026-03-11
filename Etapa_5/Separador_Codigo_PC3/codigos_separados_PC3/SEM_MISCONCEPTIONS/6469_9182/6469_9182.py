from math import *

# faça seu código aqui!

lado = float(input( " lado: " ))

apotema_1 = 2 * tan(pi/6)
apotema = lado / apotema_1

area = 3 * lado * apotema

print(round(area , 2 ))