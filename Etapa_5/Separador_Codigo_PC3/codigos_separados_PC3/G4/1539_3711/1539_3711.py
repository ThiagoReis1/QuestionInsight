from math import*
x = float(input ("digite o valor de x: "))
k = int(input("insira a quantidade de termos da serie: "))

i = 0

while(-1<x and x<1 and k>0):
	x = i - x**1 + x**2 - x**3 + x**4
	i= i+1
	
print(round())