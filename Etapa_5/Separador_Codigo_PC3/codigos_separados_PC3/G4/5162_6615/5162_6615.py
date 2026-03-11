from math import *

b = float(input("digite a estimativa de acaizeiros no campo: "))
a = float(input("digite o comprimento da aresta do hexagonal: ")) 

A = 3 * sqrt(3*(a**2))/2

tt = A * b

print(int(tt))