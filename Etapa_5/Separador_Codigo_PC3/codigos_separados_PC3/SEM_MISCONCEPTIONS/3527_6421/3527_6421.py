from math import *
termo = float(input("numero real: "))
k = int(input("numero k: "))
denominador = 0
e = 0 
while(denominador < k):
	e = e + (termo**denominador) / factorial(denominador)
	denominador = denominador + 1
	
print(round(e, 9))	