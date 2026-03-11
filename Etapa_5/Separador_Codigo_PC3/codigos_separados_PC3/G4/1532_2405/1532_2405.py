from math import*

x = float(input("digite x: "))
k = int(input("digite k: "))

varC = x
exp = 3
i = 1
while( i < k):
	varC = varC + x**exp/factorial(exp)
	
	i = i + 1
	exp = exp + 2
	
print(round(varC ,9))

	
	