from math import*

x = float(input())
k = int(input())

n = 0
qtd = 1
cos = 0

while (qtd <= k):
	qtd = qtd + 1
	cos = cos + (x**(n))/factorial(n)
	n = n + 2
	
print(round(cos,8))