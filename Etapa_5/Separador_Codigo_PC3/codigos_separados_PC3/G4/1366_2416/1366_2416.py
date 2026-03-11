from math import*
Af=radians(float(input("angulo em rads ")))
Vi=(float(input("Velocidade inicial flecha ")))
g=(9.8)
d=((Vi**2)*sin(2*Af))/g
print(round( d,2))