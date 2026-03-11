b = float(input("lado b "))
c = float(input("lado c "))

from math import radians
from math import cos
from math import sqrt

y = radians(float(input("angulo ")))

x = sqrt(b**2+c**2-(2*b*c*cos(y)))

print(round(x, 2))