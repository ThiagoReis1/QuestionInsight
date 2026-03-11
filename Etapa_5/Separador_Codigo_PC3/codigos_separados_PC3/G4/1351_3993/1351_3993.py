from math import*
m = float(input("Macas por metro quadrado: "))
a = float(input("Comprimento da aresta: "))
h = 3*(sqrt(3*a**2))/2
t = h*m
print(int(t))