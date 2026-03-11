from math import*
x = float(input("valor de x: "))
k = int(input("valor de k: "))

i = 0
soma = 0

while(k > 0):
	soma = soma + x/(factorial(2*i+1))
	k = k - 1
	i = i + 1
print(round(soma, 8))