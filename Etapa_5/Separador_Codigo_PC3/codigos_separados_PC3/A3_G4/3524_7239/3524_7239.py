from math import*
x= float(input("Qual o valor de x? "))
k= int(input("Qual o valor de k? "))
x= 0
k= 0
k= k*2
cosx= 0
cont_t= 0

while x != k:
	cosx= cosx+ ((x**k)/factorial(k))
	x= x + 1
print(round(cosx, 8))