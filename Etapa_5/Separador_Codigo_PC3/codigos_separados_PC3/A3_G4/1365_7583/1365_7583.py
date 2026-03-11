from math import radians
from math import sin
from math import sqrt
a = float(input("angulo: "))					 
b = float(input("distancia: "))
x = radians(a)
y = sqrt((b* 9.8)/(sin(2*a)))
print(round(y,2))
