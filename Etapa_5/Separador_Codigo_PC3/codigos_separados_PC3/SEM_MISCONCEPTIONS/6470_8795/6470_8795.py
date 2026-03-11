from math import *

comprimento = float(input("lado: "))
apotema = (comprimento)/(2*tan(pi/7))
area = (7*comprimento*apotema)/2


print(round(area,2))