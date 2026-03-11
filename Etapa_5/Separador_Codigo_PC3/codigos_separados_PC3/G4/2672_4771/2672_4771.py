from math import * 
r = float(input("digite o raio: "))
n = int(input("digite o numero de lados: "))
x = (1/2 *((r * cos(pi/n))**2 * tan(pi/n)))
print(round(x ,2))