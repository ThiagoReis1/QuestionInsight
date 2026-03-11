from math import *

x = eval(input())
k = int(input())
i = 1
e = 2

aux = 1

while i < k:
	if (i%2 == 0):
		aux = aux + (x**e)/factorial(e)
		e = e + 2
		i = i + 1
	else:
		aux = aux - (x**e)/factorial(e)
		e = e + 2
		i = i + 1
		
print(round(aux,10))
	
	

	