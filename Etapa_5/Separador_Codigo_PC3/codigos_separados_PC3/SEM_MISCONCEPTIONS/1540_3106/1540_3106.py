from math import *
angulo = eval(input("Angulo: "))
termos = int(input("Quantidade de termos: "))

eq = 0
exp = 0
den = 0
i = 0

while(i<termos):
	eq = eq + ( ((-1)**exp)*(angulo**exp) )/ factorial(den)
	exp = exp + 1
	den = den + 2
	
	i = i + 1
	
print(round(eq,6))

	