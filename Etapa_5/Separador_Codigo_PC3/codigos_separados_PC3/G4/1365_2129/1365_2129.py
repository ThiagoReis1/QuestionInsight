from math import *
Ang = float(input("Ângulo: "))
X = radians(Ang)
Dist = float(input("Distância: "))	
G = 9.8
v = sqrt((Dist*G)/sin(2*X))
print (round(v,2))