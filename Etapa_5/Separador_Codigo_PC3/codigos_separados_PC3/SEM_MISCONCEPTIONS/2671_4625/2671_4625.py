r = float(input("raio"))
n = int(input("lados"))

import math
apotema = r*math.cos(math.pi/n)
print(round(apotema,2))