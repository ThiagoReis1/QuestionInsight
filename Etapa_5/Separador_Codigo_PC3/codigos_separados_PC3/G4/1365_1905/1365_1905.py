from math import *
a = radians(float(input("Ângulo:")))
d = float(input("Distância:"))
Vo = sqrt(d*(9.8/(sin(2*a)))) 
print(round(Vo,2))
