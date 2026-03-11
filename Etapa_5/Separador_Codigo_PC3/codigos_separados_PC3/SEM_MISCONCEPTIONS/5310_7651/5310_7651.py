from math import*
n = float(input())
k = int(input())

cont = 0
impar = 1
result = 0

while(cont != k):
	inferior = factorial(impar)
	result += n/inferior
	impar += 2
	cont += 1

print (round(result, 8))	