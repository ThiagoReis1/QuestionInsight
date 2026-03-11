from math import *

#COMPRIMENTO DO OCTOGONO
comp8 = float( input() )


apotema = (comp8) / ( 2 * (tan( pi/8 )) )

area8 = 4 * comp8 * apotema

print(round(area8, 2))