from math import*
n = float(input("Informe o valor de n: "))
s = 0
x = 1
i = 1
valor = 3
while(i <= n):
	if(i % 2 == 1):
		s = s +(i**2 /factorial(x + valor))
	else:
		s = s -(i**2 /factorial(x + valor))
	i = i + 1
	valor = valor + 2
print(round(n,7))