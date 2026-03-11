
a = float(input("Angulo:  "))
b = float(input("Velocidade inicial:  "))
from math import radians 
from math import sin
c = radians(a)
g = 9.8
d = b**2 * ( sin(2 * c))/g
print(round(d , 2))