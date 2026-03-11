r = float(input('raio:'))
n = int(input('n de lados:'))

from math import*

A = (1/2)*(((r*cos(pi/n))**2)*(tan(pi/n)))

print(round(A, 2))