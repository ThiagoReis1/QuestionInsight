from math import*
raio=float(input())
lados=int(input())
area=1/2*((raio*cos(pi/lados))**2)*(tan(pi/lados))
print(round(area, 2))