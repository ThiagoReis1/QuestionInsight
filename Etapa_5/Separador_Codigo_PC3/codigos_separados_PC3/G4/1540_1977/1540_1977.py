from math import*
ang = eval(input())
num = int(input())
j = 2
i = 0
k = 0
valor = 0
while (i <= num):
	valor = valor + (((-1)**j)*ang**(i))/factorial(k)
	i = i + 1
	j = j + 1
	k = k + 2
print(round(valor,6))