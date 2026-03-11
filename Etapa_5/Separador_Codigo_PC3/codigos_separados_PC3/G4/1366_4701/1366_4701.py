from math import*

ang= radians(float(input("angulo")))
vel= float(input("velocidade"))
g=9.8
d= vel**2  * ((sin(2*ang)) / g)

print(float(round(d , 2)))