from math import *
x = float(input("Numero: "))
k = int(input("Qtd de termos: "))
cont = 0
pos = 0
acm = 0
while(pos < k):
	y = (x ** cont) / factorial(cont)
	cont += 1
	pos += 1
	acm = acm + y
	
print(round(acm,9))		