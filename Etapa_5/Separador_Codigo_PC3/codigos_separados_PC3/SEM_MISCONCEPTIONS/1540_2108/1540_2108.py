from math import*
x = eval(input("Numero real: "))
k = int(input("Termos da serie: "))

cont = 2
soma = 0
cima = 1
baixo = 2
sinal = 1

while cont < k:
	soma = soma + sinal*(x**cima)/factorial(baixo)
	cima =  cima + 1
	baixo = baixo + 2
	sinal = -sinal
	cont = cont + 1
total = (1 - soma)

print(round(total,6))