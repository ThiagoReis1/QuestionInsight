from numpy import *

vet = array(eval(input()))

i = 0
pontos = 0

while i < size(vet):
	if vet[i] == 1:
		pontos += 80
	elif vet[i] == 2:
		pontos += 40
	elif vet[i] == 3:
		pontos += 20
	elif vet[i] == 4:
		pontos += 10
	i += 1

print(pontos)