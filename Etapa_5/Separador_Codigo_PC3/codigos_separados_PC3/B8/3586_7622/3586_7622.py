from numpy import *

vet = array(eval(input("numeros: ")))

i = 0
pontos = 0

while i < size(vet):
	if vet[i] == 1:
		pontos = pontos + 100
	elif vet[i] == 2:
		pontos += 60
	elif vet[i] == 3:
		pontos += 20
	elif vet[i] == 4:
		pontos += 0
	i += 1
print(sum(pontos))