from math import *
k = int(input("Qual o valor de N:"))
if (n != 0):
	e = 1
	cont  = 1
	while (cont < k):
		e = e + (1/factorial(cont))
		cont = cont + 1
else:
		e = 0
print(round(e,8))