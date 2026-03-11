from math import *

# faça seu código aqui!

comprimento = float(input("Lado do decagono : "))

apotema = comprimento/(2*tan(pi/10))

Area = 5*comprimento*apotema

print(round(Area, 2))