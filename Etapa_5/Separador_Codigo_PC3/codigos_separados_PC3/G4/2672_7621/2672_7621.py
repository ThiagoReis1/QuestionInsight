from math import pi
from math import cos
from math import tan

r = float(input("Qual o raio:?"))
n = float(input("Numero de lados:?"))

area = (1/2) *(r*cos(pi/n))**2 * tan(pi/n)
print(round(area , 2))









