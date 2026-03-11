from math import*
x = float(input())
k = int(input())

n = 0
soma = 0

while k > 0:
	soma = soma +((x**2)/factorial(n + 2))
	n = n + 1
print(round(1 + soma, 9))	
	
