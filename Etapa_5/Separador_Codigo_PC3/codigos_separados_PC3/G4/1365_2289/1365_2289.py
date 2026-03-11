from math import *
a = radians(float(input("qual é o ângulo?")))
d = float(input("qual é a distância?"))
g = 9.8

from math import *
vo = (sqrt((d * g) / (sin(2 * a))))
print(round(vo, 2))