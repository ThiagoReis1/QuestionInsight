from math import tan
from math import pi

comprimento = float(input("comprimentos lado do pentagono"))

Apotema = comprimento / (2*tan(pi/6))

area = 3 * comprimento * Apotema

print(round(area,2))