from math import *

# comprimento do lado do octogono 
lado = float((input( "digite o lado do octogono:")))
# apotema
apotema = lado / (2* tan(pi/8))
#area do octogono
area_octogono = 4 * lado * apotema 
# resultado arredondado
print(round(area_octogono, 2))