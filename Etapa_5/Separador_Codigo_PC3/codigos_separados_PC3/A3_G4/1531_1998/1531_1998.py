from math import *
x = eval (input("digite o angulo: "))
k = float (input("digite o Nr: "))
i = 1
soma = 0
total = 1.0
d = 2
while (i<k) :
	soma = (-1)**i*(x**(d))/factorial(d)
	total = total + soma
	i = i + 1
	d = d + 2
print (round(total,10))