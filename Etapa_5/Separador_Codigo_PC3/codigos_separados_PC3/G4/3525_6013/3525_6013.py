from math import*

x = float(input())
k = int(input())
c =1 
soma = 0
while (k!= 0):
	k = k -1 
	soma=soma+((x**c)/factorial(c))
	c = c +2

print(round(soma,9))
