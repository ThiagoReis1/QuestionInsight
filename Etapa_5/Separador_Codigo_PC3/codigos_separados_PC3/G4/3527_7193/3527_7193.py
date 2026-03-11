from math import*

x = float(input("informe o numero real x: "))
k = int(input("informe a quantidade de termos: "))

cont = 0
e = 0 
v = 0
while (cont < k):
	e = e + ((x**v)/factorial(v))
	cont = cont + 1
	v = v + 1
print(round(e,9))