from math import *

# Entradas

LB = float(input("Lado B:"))
LC = float(input("Lado C:"))
Ang = radians(float(input("Angulo entre B e C:")))

# Calculo 

A = sqrt(LB**2 + LC**2 - 2*LB*LC*cos(Ang))

# Saida 

print(round(A,2))