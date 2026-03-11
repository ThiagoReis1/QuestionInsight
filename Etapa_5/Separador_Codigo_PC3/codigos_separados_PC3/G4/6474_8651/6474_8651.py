from math import tan
from math import pi

c = float(input("comprimento do lado:"))
apo = c / (2 * tan(pi/11))
area = (11 * c * apo)/ 2

print(round(area,2))