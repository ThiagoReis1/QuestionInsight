from numpy import *

pontos = array(eval(input()))

cont = 0
soma = 0

while cont < size(pontos):
	if pontos[cont] == 1:
		soma += 80
	elif pontos[cont] == 2:
		soma += 40
	elif pontos[cont] == 3:
		soma += 20
	elif pontos[cont] == 4:
		soma += 10
	cont += 1
	
print(soma)