from math import *

a = eval(input("valor do angulo x: "))
n = int(input("valor do numero k: "))

soma = 1
i = 0


while(a > n):
	soma = soma - (i**2/factorial(2) + i**4/factorial(4))
	i = i + 2

print(round(soma, 10))

	
