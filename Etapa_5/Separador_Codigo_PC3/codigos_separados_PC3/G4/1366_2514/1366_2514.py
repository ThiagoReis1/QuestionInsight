from math import sin 
from math import radians
a = radians(float(input(" angulo ")))
v = float(input(" velocidade inicial "))

gravidade = 9.8
d = (v ** 2) * (sin(2 * a)) / gravidade 


print(round(d,2)) 