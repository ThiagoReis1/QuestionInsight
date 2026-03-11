r = float(input("Insira o valor do raio "))
n = int(input("Insira o numero de lados "))
import math
A = 0.5*((r*math.cos(math.pi/n))**2)*math.tan(math.pi/n)
print(round(A,2))