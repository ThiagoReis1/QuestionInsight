from math import*
T = float(input("Digite o periodo de oscilacao do pendulo: ")) 
g = 9.81
L = float (g * (T/(2*pi))**2)
print (L)