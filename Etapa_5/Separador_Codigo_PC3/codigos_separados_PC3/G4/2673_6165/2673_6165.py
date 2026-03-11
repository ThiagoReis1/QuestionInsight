from math import * 

r = float(input("Qual o valor de r?: "))
n = float(input("Qual o numero de lados n do poligano?: "))

l = 2*r*sin(pi/n)

print(round(l, 2))
