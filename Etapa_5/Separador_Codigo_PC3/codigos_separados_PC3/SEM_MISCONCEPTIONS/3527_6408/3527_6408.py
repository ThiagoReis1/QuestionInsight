from math import *
termo = float(input("numero de real: "))
k = int(input("numero de k: "))
e = 0
denominador = 0
while(denominador < k):
	e = e + (termo**denominador) / factorial(denominador) 
	denominador = denominador + 1
	
print(round(e, 9))