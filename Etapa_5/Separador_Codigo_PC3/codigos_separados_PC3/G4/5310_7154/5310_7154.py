from math import*


x = float(input("numero real: "))
k = int(input("quantidade de termos: "))

n = 0
p = 0

while(n < k):
	p = p + (x / factorial(2 * n + 1))
	n = n + 1

print(round(p,8))
	