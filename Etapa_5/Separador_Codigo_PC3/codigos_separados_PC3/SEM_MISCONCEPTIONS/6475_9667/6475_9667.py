from math import *

lado =int(input(" entre com o comprimento do lado:"))

apotema= lado /(2* tan(pi/12))

areaD= 6 * lado * apotema

print(round(areaD,2))