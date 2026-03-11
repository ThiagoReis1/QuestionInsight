
from math import *

ang = radians(float(input("digite o angulo : ")))
vel = float(input("digite a velocidade : "))

g = 9.8
d = vel ** 2 * sin(2 * ang) / g

total = print(round(d, 2))