from math import *
n = int(input("Digite o valor da qtd de casas de aproximacao: "))
h = 1
y = 3
x = 0
soma = 0
while (n > x):
	valor = (((-1) ** h) * sqrt(h)) / (6+y)
	soma = soma + valor
	h = h + 1
	y = y + 2
	x = x + 1
print (round(soma, 5))