from math import*

angulo = eval(input("angulo: "))
n = int(input("k: "))
cos = 1
cont = 0
d = 2

while(cont<n):
	cos = cos +((angulo**d)/(factorial(d)))*(-1**cont)
	cont = cont + 1
	d = d + 2
	
print(round(cos,10))
