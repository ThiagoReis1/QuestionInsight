from math import *
angulo = float((input("Digite um numero: ")))
k = int((input("Digite o numero de termos:")))

soma = angulo
i = 1
while (i < k):
	soma = soma + (angulo ** ((2 * i) + 1)) / factorial((2 * i) + 1)
	i = i + 1
	
print(round(soma,9))

n = int(input("Digite o numero: "))
i = 1
acum = 0
while i <= n:
	if n % i == 0:
		print(i)
		acum = acum + 1
	
	i = i + 1
if acum == 1:
	print(acum, "divisor")
else:
	print(acum, "divisores"