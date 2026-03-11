from math import *

# faça seu código aqui!

lado_dodecagono = float(input("Entre com o valor do lado do dodecagono = "))

apotema = (lado_dodecagono) / (2 * tan(pi/12))

area_dodecagono = 6 * lado_dodecagono * apotema

print(round(area_dodecagono , 2))
