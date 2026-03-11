from math import radians 
from math import sin
a = float(input("ang: "))
d = float(input("distancia: "))
c = a
g = 9.8
vi = 1 ** (d * (g // sin(2 * c)))
print(round(vi,2))
