from math import*
x = int(input("Digite valor de x: "))
k = int(input("Digite valor de k: "))
acum = 1 + x
cont = 2
t = 2

while t > x:
	den = factorial(cont)
	expt = x ** t
	acum = acum + (expt/den)
	t = t + 1
	cont = cont + 1
	
	print(round(acum, 9))
