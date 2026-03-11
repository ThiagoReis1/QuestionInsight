from math import*
x = float(input("Numero real: "))
k = int(input("Quantidade de termos: "))
i = 0
f = 0
p = 0
e = 0

while (i < k):
	e = (e + ((x**p)/factorial(f)))
	p = p + 1
	f = f + 1
	i = i + 1
	
print(round(e, 9))